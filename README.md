FT_TRANSCENDENCE


Project Overview

ft_transcendence is a web application designed for the mighty Pong contest! The goal is to allow users to play real-time multiplayer Pong with other participants. The project emphasizes both frontend and backend development, with a focus on providing a smooth user experience and enhanced features such as AI opponents, tournaments, and advanced 3D rendering.


Features
---------------------------
This project adheres to the mandatory technical requirements, while incorporating additional modules to enrich the user experience and expand functionality.

---------------------------
Mandatory Features

-Single Page Application: The website is designed as a single-page application, ensuring seamless user interaction with minimal page reloads.
-Vanilla JavaScript Frontend: The frontend is developed in vanilla JavaScript, guaranteeing compatibility with the latest version of Google Chrome.
-Real-Time Multiplayer Pong: Users can participate in live Pong games directly on the website, playing against other users.
-Tournament System: Users can join tournaments, with the system organizing matches and determining winners.
-Registration & Matchmaking: Players register with an alias for each tournament, and matchmaking ensures a fair and competitive environment.
-Dockerized Deployment: The entire website runs in a containerized environment, using Docker to ensure smooth deployment and security.
-Additional Modules
---------------------------

---------------------------
To enhance the project, we have integrated the following modules:

-Backend Framework: Instead of using pure Ruby, we are leveraging a backend framework to handle server-side logic more efficiently.
-Database Integration: A robust database is used to store essential information such as user data, tournament progress, and game statistics.
-Frontend Framework: We opted to use a frontend framework/toolkit to streamline the development of the user interface and improve scalability.
-Standard User Management: We have implemented a full-fledged user management system, allowing for user registration, authentication, and tournament participation tracking.
-Remote Players: Players can compete against each other remotely, adding an online multiplayer dimension to the Pong experience.
-AI Opponent: We’ve implemented a computer-controlled AI opponent, allowing users to practice or compete when no human opponents are available.
-Advanced 3D Techniques: The game visuals have been enhanced with 3D rendering techniques, providing a modern and visually appealing version of Pong.
-Server-Side Pong: Instead of relying on client-side game logic, the game mechanics are processed on the server, improving fairness and synchronizing game state across players.
-API Implementation: We’ve implemented a comprehensive API that facilitates communication between the server and clients, allowing for real-time game updates and remote gameplay.
-Extended Browser Compatibility: While we focus on Chrome compatibility, we’ve extended support to other modern browsers to ensure a broader reach.
-Server-Side Rendering (SSR): We’ve integrated server-side rendering to improve performance and SEO, ensuring that the website is fast and responsive across devices.
-Security
-Security is a critical concern for this project:
---------------------------


-Password Hashing: All user passwords are hashed before storage.
-Protection Against SQL Injection/XSS: The website is safeguarded against common web vulnerabilities such as SQL injection and cross-site scripting.
-HTTPS and WSS: The entire site, including websockets, operates over secure HTTPS and WSS protocols.
-Form Validation: All user inputs are validated either on the frontend or backend to ensure data integrity and prevent malicious inputs.
-Environment Variables: Sensitive information such as API keys and credentials are securely stored in environment variables, which are not included in version control.

Conclusion

ft_transcendence takes the classic Pong game to the next level with multiplayer capabilities, tournaments, AI opponents, and cutting-edge 3D graphics. Through modular development and strong security practices, this project delivers a modern and robust gaming experience.