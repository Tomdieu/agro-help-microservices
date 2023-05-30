FROM node:20.1-alpine3.16

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy the rest of the app files
COPY . .

# Build TypeScript code
RUN npm run build

# Expose the port
EXPOSE 5000

# Start the app
CMD ["npm", "start"]