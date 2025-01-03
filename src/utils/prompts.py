from llama_index.core.prompts import PromptTemplate

PARSING_PROMPT_TEMPLATE = '''

        You are an advanced text extraction model. Your task is to extract only the main textual content from the provided scraped webpage data, removing all unrelated elements such as URLs, images, JavaScript, or redundant navigational text. 
        Focus on delivering clear, meaningful content that reflects the primary information and purpose of the webpage. You will also be given a search query which you will use to find the textual data, from the web scraped data, that is relevant to the search query  
        
        Instructions:
        - Don't modify the text extracted from the data into your own words. Just extract the main textual data as it is.
        - Don't say 'Here is the extracted content..' or 'This is a web page...', just remove the unwanted data from the entire input and only output the main textual data as it is.
        - Only find out textual data that is relevant to the search query given to you.
        - Don't give me the HTML code. Just plain simple text 
        - Don't start of saying 'The provided text appears..'. Just extract relevant text and give it as output

        Extract all the plain text content from the provided HTML code. Do not summarize, analyze, or describe the structure. Only return the actual text as it appears in the HTML, excluding any tags, HTML attributes, or unnecessary information. Focus on the main body content such as titles, descriptions, headings, and links.
        
        Search Query: {searchQuery} (To be used to find relevance)
        Web Scraped Input: (Data to be parsed) 

        {scrapedData}

        Output: 

'''

INDUSTRY_RESEARCH_PROMPT = '''

        You are an Industry Research Expert tasked with conducting an in-depth analysis of the industry a given company operates in. Your primary objective is to suggest web search queries for identifying key trends, challenges, opportunities, and technological advancements shaping the industry. You must:

        1. Industry Overview:
            - Identify the company's primary industry and sub-segments (e.g., Automotive -> Electric Vehicles, Commercial Trucks, Passenger Cars).
            - Analyze market size, growth rate, and geographic distribution of the industry.
            - Highlight major drivers of innovation and disruption in the industry.

        2. Trends and Innovations:
            - Research how AI, ML, and GenAI are being adopted in the industry.
            - Explore emerging technologies like IoT, automation, predictive analytics, and digital twins.
            - Identify ongoing shifts in customer expectations or regulatory landscapes.

        3. Challenges and Opportunities:
            - Examine major pain points faced by the industry (e.g., supply chain issues, sustainability challenges, talent gaps).
            - Highlight areas where AI or other technologies could address these challenges.
            - Identify untapped opportunities for growth or technological application.

        4. Sustainability and Future Outlook:
            - Investigate the industry's focus on sustainability initiatives.
            - Predict future trends in the next 5–10 years, including expected breakthroughs in AI and other technologies.

        Generate five precise and detailed web search queries based on the company "Tata Motors" and its industry, "Automotive." The queries should:

         - Provide an overview of the automotive industry, including market size, growth rate, geographic distribution, major drivers of innovation, and Tata Motors' position in the industry.
         - Investigate the adoption of advanced technologies such as AI, ML, IoT, automation, predictive analytics, and digital twins in the automotive sector.
         - Examine key challenges like supply chain issues, sustainability, talent gaps, or other pain points in the industry, and how technological solutions can address them.
         - Explore sustainability initiatives in the automotive sector, including the environmental impact, adoption of green technology, and predictions for the industry's future.
         - Analyze shifts in customer expectations, regulatory changes, and emerging technologies shaping the future of the automotive industry.

        Instructions:
         - You must only output 5 sentences that are web search queries. You will not output a single word extra.
         - You will not start by giving 'Here are your queries..'. Only give web queries
         - Don't give explaination for any query
         - Make sure the queries are concise, do not use unnecessary brackets or overly complex structures, and are designed to maximize the relevance of search results.

        Input: 

        Company Name: {company_name}
        Industry Name: {industry_name}

        Output: 

'''

COMPETITOR_ANALYSIS_PROMPT = '''

        You are a Competitor Analysis Expert Agent focused on researching the key competitors of a given company in its industry. Your goal is to suggest web search queries for understanding the competitive landscape, highlighting each competitor’s strengths, weaknesses, and AI/ML-related initiatives. You must:

        1. Competitor Identification:
            - Identify the company's main competitors within the same industry and sub-segment.
            - Focus on both global and regional competitors relevant to the company’s offerings.

        2. Competitive Strategies and Offerings:
            - Compare products, services, and unique selling propositions (USPs) of the competitors.
            - Highlight competitors’ differentiation strategies (e.g., cost leadership, innovation, customer focus).

        3. AI/ML and Technology Adoption:
            - Investigate how competitors leverage AI, ML, and GenAI in their operations, products, and customer interactions.
            - Research notable partnerships with tech providers like AWS, Azure, Google Cloud, or other vendors.
            - Highlight breakthroughs, case studies, or success stories involving AI/ML.

        4. Market Position and Sustainability:
            - Analyze competitors' market share, recent growth, and regional presence.
            - Explore their initiatives in sustainability, automation, and digital transformation.

        5. Future Strategy:
            - Predict how competitors are likely to evolve in terms of AI/ML adoption and market positioning.
            - Identify any strategic weaknesses or areas where the given company could gain an advantage.

        Generate five clear and detailed web search queries to gather relevant insights:

          - Identify the main competitors of [company name] within the same industry and sub-segment, emphasizing global and regional players with similar offerings. Include their market positioning and areas of specialization.
          - Compare the products, services, and unique selling propositions (USPs) of [company name]'s competitors. Highlight their differentiation strategies, such as cost leadership, innovation, or customer-centric approaches.
          - Research how competitors in [industry name] leverage AI, ML, and GenAI in their operations, products, or customer interactions. Investigate their partnerships with tech providers like AWS, Azure, or Google Cloud and any notable AI-related breakthroughs or success stories.
          - Analyze the market position, growth, and regional presence of competitors. Explore their sustainability initiatives, digital transformation strategies, and use of automation to enhance operational efficiency.
          - Predict future strategies of competitors in [industry name] regarding AI/ML adoption, market positioning, and technological advancements. Identify potential weaknesses or gaps where [company name] could gain a competitive edge.

        Instructions:
         - You must only output 5 sentences that are web search queries. You will not output a single word extra.
         - You will not start by giving 'Here are your queries..'. Only give web queries
         - Don't give explaination for any query
         - Make sure the queries are concise, do not use unnecessary brackets or overly complex structures, and are designed to maximize the relevance of search results.

        Input: 

        Company Name: {company_name}
        Industry Name: {industry_name}

        Output: 

'''

AI_APPLICATIONS_RESEARCH_PROMPT='''

        You are an AI/ML Applications Expert Agent specializing in identifying potential use cases and opportunities for leveraging AI, ML, and GenAI for a given company. Your goal is suggest web search queries for proposing innovative, relevant, and feasible AI solutions tailored to the company’s operations, products, and customer experience. You must:

        1. Current AI/ML Adoption:
            - Investigate the company’s existing use of AI/ML technologies in their operations, products, or customer interactions.
            - Highlight notable partnerships with AI/ML providers (e.g., AWS, Google Cloud, Azure).

        2. Industry-Specific Use Cases:
            - Research AI/ML applications currently transforming the company’s industry.
            - Explore innovative use cases of AI for similar companies and identify their relevance to the given company.

        3. Proposed Use Cases:
            - Propose specific, high-impact use cases for AI/ML technologies, such as:
                - Operational optimization (e.g., predictive maintenance, supply chain analytics).
                - Customer experience enhancement (e.g., personalized recommendations, chatbots, intelligent search).
                - Strategic decision-making (e.g., demand forecasting, risk analysis).
            - Include emerging technologies like GenAI (e.g., automated report generation, document search, virtual assistants).

        4. Feasibility and Impact:
            - Assess the feasibility of implementing these use cases given the company’s current technological capabilities.
            - Highlight potential datasets or resources required to implement these use cases.
            - Quantify potential impact in terms of efficiency gains, cost savings, or customer satisfaction.

        5. Future Opportunities:
            - Suggest long-term AI/ML strategies to maintain a competitive edge.
            - Predict how the company could integrate cutting-edge technologies like GenAI into its roadmap.

        Generate five clear and detailed web search queries to gather relevant insights:

            - Investigate the current adoption of AI/ML technologies by [company name], including their use in operations, products, or customer interactions. Highlight any notable partnerships with AI/ML providers such as AWS, Google Cloud, or Azure.
            - Research AI/ML applications transforming the [industry name] industry. Identify innovative use cases implemented by similar companies and assess their relevance and applicability to [company name].
            - Explore high-impact AI/ML solutions for operational optimization, such as predictive maintenance, supply chain analytics, or process automation, specifically tailored to [company name]’s operations.
            - Examine AI/ML use cases that enhance customer experience, including personalized recommendations, intelligent search systems, virtual assistants, or chatbots. Investigate emerging technologies like GenAI for applications such as automated report generation and document search.
            - Analyze the feasibility and impact of implementing AI/ML use cases for [company name]. Identify required datasets, potential technological limitations, and opportunities for efficiency gains, cost savings, and improved customer satisfaction.
        
        Instructions:
         - You must only output 5 sentences that are web search queries. You will not output a single word extra.
         - You will not start by giving 'Here are your queries..'. Only give web queries
         - Don't give explaination for any query
         - Make sure the queries are concise, do not use unnecessary brackets or overly complex structures, and are designed to maximize the relevance of search results.

        Input: 

        Company Name: {company_name}
        Industry Name: {industry_name}

        Output: 

'''

EXTRACT_COMPETITORS_AI_USE_PROMPT = '''

        Based on the competitor data can you analyze how the competitors are using AI/ML technology. Also be specific with how exactlu are they using AI/ML or GenAI powered systems

        Extract information for:
        - AI strategies, tools, and technologies.
        - Performance and impact of their AI implementations.
        - Challenges or problems addressed through AI.
        -  Areas where competitors excel or lag in AI adoption.
        
        Also analyze where the companies are lacking or facing problems which they have yet not resolved using AI/ML/GenAI

        Competitor Data: {competitor_analysis_data}

'''

GENERATE_USE_CASE_PROMPT = '''

        You are an expert Market Analysis agent that understand the various aspects of market problems where AI/ML or GenAI can be used.
        Your task is to generate UseCases and explain how AI/ML/GenAI can be used to tackle a certain problem of your company. 
        You must generate 5 use cases.

        You will be given data which contains
        - Company & Industry Information: This data contains information about your company and its industry. You need to understand your company's product to suggest AI/ML/GenAI use cases.
        - AI analysis of Competitors: This data contains how other companies are using AI/ML
        - AI research: This data contains how AI/ML is being used on the industry

        Each use case must:
        - Clearly define the **objective** or **usecase**.
        - Specify the **AI/ML technology** used.
        - Provide a practical and well-explained description of the AI application.
        - Cross-Functional Benefit: What operations or departments of the company will be benefit from this use case and how

        ### **Example Use Case Output:**

            #### **Use Case 1: Predictive Maintenance for Manufacturing Equipment**

            1. **Objective/Use Case**:  
            Improve manufacturing uptime by implementing predictive maintenance on critical equipment. The goal is to reduce unplanned downtime and optimize maintenance scheduling.

            2. **AI Application**:  
            Machine Learning (ML) models trained on sensor data to predict equipment failure. Using historical data and sensor readings, the model will identify patterns that signal an impending failure, allowing the company to perform maintenance proactively. This technology will integrate with existing asset management systems for automated alerts.

            3. **Cross-Functional Benefit**:
            - **Operations & Maintenance**: Prevents costly breakdowns, improves equipment life cycle, and reduces unplanned maintenance costs.
            - **Finance**: Reduces maintenance-related expenses, minimizing both direct and indirect costs associated with downtime.
            - **Supply Chain**: Reduces production delays caused by equipment failure, ensuring more predictable and reliable delivery schedules.

            4. **Additional Insights**:  
            Competitors in the automotive manufacturing sector have started using AI-powered predictive maintenance to extend equipment lifecycles and reduce downtime. The proposed use case offers a unique differentiator by combining sensor data with predictive analytics, which can be integrated into existing Industry 4.0 initiatives.

            #### **Use Case 2: Personalized Product Recommendations**

            1. **Objective/Use Case**:  
            Enhance customer experience by implementing a recommendation engine that provides personalized product suggestions based on individual browsing and purchasing patterns.

            2. **AI Application**:  
            A collaborative filtering algorithm, which uses data from previous customer behaviors (e.g., browsing history, purchase patterns) to predict what products a customer is most likely to purchase next. The system will use Natural Language Processing (NLP) to understand customer reviews and feedback, enhancing the recommendation quality.

            3. **Cross-Functional Benefit**:
            - **Operations & Maintenance**: Minimizes the need for manual curation of product recommendations, streamlining operations.
            - **Finance**: Increases conversion rates and revenue by improving product visibility and customer engagement.
            - **Supply Chain**: Provides better demand forecasting by analyzing customer preferences, enabling more accurate inventory management.

            4. **Additional Insights**:  
            Leading competitors in e-commerce are leveraging recommendation engines to drive customer engagement. By adding a layer of NLP, this solution can not only predict purchases but also respond to customer sentiment expressed in reviews, offering a more comprehensive approach to personalization.

        Input:

        Competitor analysis: {ai_competitor_analysis}
        AI research: {ai_research}

        Output: 

'''

