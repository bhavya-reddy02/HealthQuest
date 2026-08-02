FROM node:20-alpine

WORKDIR /app

# Copy package descriptors first to cache npm install layer
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose Vite's default dev port
EXPOSE 5173

# Start the dev server with host binding using npx
CMD ["npx", "vite", "--host", "0.0.0.0"]
