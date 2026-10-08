---
id: TC-AUTH-LP-E2E-018-resilience-pencatatan-audit-log
title: Ketahanan sistem saat layanan penulisan audit log mengalami gangguan
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-130
  - TC-AUTH-LP-153
coverage:
  web: automated
---

# Ketahanan sistem saat layanan penulisan audit log mengalami gangguan

## Prerequisites

- Pengujian memerlukan dua sesi browser:
  - Sesi 1: Form Login with Password untuk submit skenario login.
  - Sesi 2: Administrator Total Control (Global Settings) yang memantau `Global Settings > Activity Log > Session`.
- User `budisantoso@qwertysystem.net` berstatus Activated dan Active dengan password `QaLogin#2026`.
- Mode: mock untuk simulasi kegagalan layanan antrian/penulisan log asynchronous di backend.

## Test Steps

### Kegagalan sementara penulisan log tidak menggagalkan login (Eventual Consistency)

1. Pada Sesi 1: Buka halaman Login with Password
2. Masukkan email `budisantoso@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA
3. Simulasikan layanan log database / background logger tidak tersedia sementara (failure injection)
4. Klik tombol [Log in]
5. Verifikasi login tetap berhasil dan browser menuju Portal — Product Hub tanpa tertahan oleh kegagalan log
6. Pulihkan layanan penulisan log
7. Pada Sesi 2: Buka `Global Settings > Activity Log > Session` dan muat ulang tabel setelah beberapa saat
8. Verifikasi entri login untuk "Budi S" berhasil muncul dengan Status "Success" dan Note "Login with password" setelah layanan pulih

### Seluruh retry penulisan log habis tidak menggagalkan login

9. Pada Sesi 1: Logout dari Portal dan kembali ke halaman Login with Password
10. Masukkan kembali email `budisantoso@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA
11. Simulasikan layanan penulisan log mati total (down lebih dari batas retry timeout, misal >13 menit)
12. Klik tombol [Log in]
13. Verifikasi login tetap berhasil menuju Portal — Product Hub dan user dapat beraktivitas normal
14. Pulihkan layanan log setelah seluruh batas retry antrian habis
15. Pada Sesi 2: Muat ulang `Global Settings > Activity Log > Session`
16. Verifikasi tidak ada entri duplikat atau crash pada tabel log, dan login user tetap valid meskipun pencatatan log gugur

## Notes

- Sesuai NC-18 dan PRD §9.4.2 / §9.6, keputusan autentikasi dan mutasi lock adalah atomik, sedangkan penulisan audit log bersifat best-effort dengan retry; kegagalan penulisan log tidak boleh menggagalkan proses login user yang kredensialnya valid.
