---
id: TC-AUTH-OTP-E2E-024-plan-gating-dan-status-client
title: "Evaluasi Plan Gating Lintas Entitas dan Penolakan Status Client Suspended/Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-144
  - TC-AUTH-OTP-145
  - TC-AUTH-OTP-146
  - TC-AUTH-OTP-147
  - TC-AUTH-OTP-148
  - TC-AUTH-OTP-149
  - TC-AUTH-OTP-150
  - TC-AUTH-OTP-151
  - TC-AUTH-OTP-152
coverage:
  web: automated
---

# Evaluasi Plan Gating Lintas Entitas dan Penolakan Status Client Suspended/Expired

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- Akun uji milik tenant Client dengan variasi paket langganan:
  - `user.starter@client-starter.com` (Plan: Starter)
  - `user.growth@client-growth.com` (Plan: Growth)
  - `user.pro@client-pro.com` (Plan: Professional)
  - `user.ent@client-ent.com` (Plan: Enterprise)
- Akun uji lintas tipe entitas non-Client:
  - `distributor.user@distributor.com` (Entitas: Distributor)
  - `partner.user@partner.com` (Entitas: Partner)
  - `principal.user@tagsamurai.com` (Entitas: Principal)
- Akun uji dengan status langganan Client bermasalah:
  - `client.suspended@suspended-co.com` (Client status: Suspended)
  - `client.expired@expired-co.com` (Client status: Expired)
- Mail-catcher aktif.

## Test Steps

### Universalitas fitur Login with OTP pada semua Tier Plan (Plan Gating N/A)

1. Buka Request OTP, masukkan `user.starter@client-starter.com`, selesaikan reCAPTCHA, klik [Request OTP]
2. Masukkan kode OTP dari mail-catcher
3. Verifikasi pengguna dengan plan Starter berhasil login tanpa pemblokiran fitur
4. Ulangi pengujian login OTP berturut-turut untuk akun ber-plan Growth (`user.growth@...`), Professional (`user.pro@...`), dan Enterprise (`user.ent@...`)
5. Verifikasi seluruh tingkat plan langganan dapat mengakses fitur Login with OTP secara penuh tanpa pembatasan

### Akses Login with OTP lintas jenis entitas organisasi

6. Masukkan email user entitas Distributor (`distributor.user@distributor.com`) ke Request OTP
7. Selesaikan OTP hingga masuk ke Portal
8. Verifikasi pengguna Distributor berhasil login
9. Ulangi proses yang sama untuk entitas Partner dan entitas Principal
10. Verifikasi seluruh entitas ekosistem TAG Samurai didukung secara seragam oleh Login with OTP

### Penolakan login untuk akun milik Client yang di-suspend

11. Buka halaman Request OTP
12. Masukkan email `client.suspended@suspended-co.com`
13. Selesaikan reCAPTCHA dan klik [Request OTP]
14. Verifikasi request ditolak oleh backend
15. Verifikasi caption error inline atau banner penolakan menampilkan pesan status: "Your client account is suspended"
16. Verifikasi kode OTP tidak dikirimkan ke email tersebut

### Penolakan login untuk akun milik Client yang masa berlakunya kadaluwarsa (Expired)

17. Masukkan email `client.expired@expired-co.com` ke Request OTP
18. Selesaikan reCAPTCHA dan klik [Request OTP]
19. Verifikasi request ditolak oleh backend
20. Verifikasi pesan penolakan menampilkan: "Your subscription has expired"
21. Verifikasi tidak ada kode OTP yang diterbitkan

## Notes

- Fitur autentikasi Login with OTP merupakan fungsi baseline platform (Tier Core) sehingga tidak ada Plan Gating (tersedia untuk Starter, Growth, Professional, dan Enterprise, serta seluruh tipe entitas).
- Status operasional entitas Client (Dimensi D1) dievaluasi di pintu masuk autentikasi; akun di bawah naungan tenant yang berstatus Suspended atau Expired diblokir dari menerbitkan OTP.
