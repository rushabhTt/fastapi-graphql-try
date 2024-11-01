### Setting Up a Virtual Environment (venv) and Managing Dependencies

Here's how you can create and manage a virtual environment, as well as install packages from `requirements.txt`:

---

#### 1. **Creating a Virtual Environment**
Open your terminal and navigate to your project folder, then use the following command:
```bash
# For Unix/macOS
python3 -m venv venv

# For Windows
python -m venv venv
```
This command creates a folder named `venv` in your project directory, containing the virtual environment.

---

#### 2. **Activating the Virtual Environment**
- **On Unix/macOS:**
  ```bash
  source venv/bin/activate
  ```
- **On Windows (Command Prompt):**
  ```bash
  venv\Scripts\activate
  ```
- **On Windows (PowerShell):**
  ```bash
  .\venv\Scripts\Activate
  ```

---

#### 3. **Deactivating the Virtual Environment**
To deactivate your virtual environment, simply run:
```bash
deactivate
```

---

#### 4. **Installing Dependencies from `requirements.txt`**
Make sure your virtual environment is activated, then run:
```bash
pip install -r requirements.txt
```

This will install all the packages listed in `requirements.txt`.

---

### GraphQL Flow - Quick Notes

1. **GraphQL Playground**
   - Browser-based tool for testing GraphQL APIs
   - Access at `http://127.0.0.1:8000/graphql`
   - Used for sending queries & viewing responses

2. **Basic Query Flow**
   ```graphql
   {
     hello
   }
   ```

3. **Step-by-Step Process**
   a. **Request Initiation**
   - Query sent as HTTP POST to `/graphql` endpoint
   - FastAPI receives request

   b. **Processing**
   - FastAPI routes to GraphQLRouter
   - Strawberry parses query
   - Resolver function executes
   - Response formatted as JSON

   c. **Response Structure**
   ```json
   {
     "data": {
       "hello": "Hello, GraphQL with FastAPI!"
     }
   }
   ```

4. **Key Components**
   - FastAPI: Main server framework
   - Strawberry: GraphQL library
   - GraphQLRouter: Bridge between FastAPI & GraphQL
   - Resolver: Function handling the query

5. **Benefits**
   - Single endpoint (`/graphql`) for all requests
   - Interactive testing via Playground
   - Flexible data retrieval
   - Client controls data shape

6. **Integration Points**
   - Strawberry handles GraphQL logic
   - FastAPI provides server infrastructure
   - GraphQLRouter manages routing
   - All requests go through `/graphql` endpoint

![Screenshot (869)](https://github.com/user-attachments/assets/922b4eb9-7f50-433a-bf59-4b2c6172a8f6)

---

### **Add a Custom Type with a Simple Query**

You can extend your GraphQL API by adding custom types for more structured and meaningful queries. Here’s how to use a custom type and query it:

1. **Custom Query Example**  
   Access your GraphQL Playground at `http://127.0.0.1:8000/graphql` and run this query:
   ```graphql
   {
     getUser {
       id
       name
       email
     }
   }
   ```
   - This query fetches `id`, `name`, and `email` fields for a user.

2. **Flexibility of Custom Queries**  
   - **Select Specific Fields**: You don't have to retrieve all fields. You can simplify your request by choosing only the ones you need.
   - Example of a selective query:
     ```graphql
     {
       getUser {
         name
       }
     }
     ```
   - This one will only return the user's name.

3. **Combining Queries**  
   You can run multiple queries at once. Here's an example:
   ```graphql
   {
     hello
     getUser {
       id
       name
       email
     }
   }
   ```
   - This will retrieve a greeting message and the user’s details.

4. **Additional Query Options**  
   You can also use queries like those shown in the image above:
   ```graphql
   {
     getUserById(id: 2) {
       id
       name
       email
     }
     allUsers {
       id
       name
       email
     }
   }
   ```
   - `getUserById`: Fetches details for a specific user by `id`.
   - `allUsers`: Retrieves a list of all users with their details.

![image](https://github.com/user-attachments/assets/b3846179-5836-4e99-82cc-2bbde717b69b)

Create a New User:
graphql
Copy code
mutation {
  createUser(name: "Daisy", email: "daisy@example.com") {
    id
    name
    email
  }
}

> Note: The mutation data will persist only while the server is running. Once the server is stopped, all created data will be lost since we're using an in-memory list instead of a persistent database.
