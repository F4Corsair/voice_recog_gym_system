# 1: Node.js 환경에서 Vite 빌드
FROM node:18 AS builder

# 작업 디렉토리 설정
WORKDIR /app

# pnpm 설치
RUN corepack enable && corepack prepare pnpm@latest --activate

# package.json과 pnpm-lock.yaml 복사
COPY package.json pnpm-lock.yaml ./

# 종속성 설치 (프로덕션 환경에서는 devDependencies 제외)
RUN pnpm install --frozen-lockfile

# 프로젝트 소스 복사
COPY . .

# Vite 빌드
RUN pnpm run build

# 2: Nginx로 정적 파일 서빙
FROM nginx:1.23

# Nginx 설정 복사
COPY nginx.conf /etc/nginx/nginx.conf

# Vite 빌드 결과를 Nginx의 정적 파일 디렉토리로 복사
COPY --from=builder /app/dist /usr/share/nginx/html

# 컨테이너 실행 시 Nginx 시작
CMD ["nginx", "-g", "daemon off;"]