/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    const api = (process.env.ARTHA_API_URL || "http://127.0.0.1:8000").replace(/\/$/, "");
    return [{source:"/api/artha/:path*",destination:`${api}/api/artha/:path*`}];
  },
};

export default nextConfig;
