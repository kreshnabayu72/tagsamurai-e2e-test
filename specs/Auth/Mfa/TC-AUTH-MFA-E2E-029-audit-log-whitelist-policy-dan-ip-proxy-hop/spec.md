---
id: TC-AUTH-MFA-E2E-029-audit-log-whitelist-policy-dan-ip-proxy-hop
title: "Audit Log: Kebijakan Whitelist Non-Logged Events dan Integritas IP Header X-Forwarded-For"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-167
  - TC-AUTH-MFA-168
  - TC-AUTH-MFA-169
  - TC-AUTH-MFA-170
  - TC-AUTH-MFA-171
  - TC-AUTH-MFA-172
  - TC-AUTH-MFA-173
  - TC-AUTH-MFA-174
coverage:
  web: automated
---
# Audit Log: Kebijakan Whitelist Non-Logged Events dan Integritas IP Header X-Forwarded-For

## Prerequisites

- Akun Total Control Global Settings untuk modul Activity Log dan User Log.
- User uji dengan akses multi-surface log.
- Reverse proxy mock untuk pengujian header `X-Forwarded-For`.

## Test Steps

### Pencatatan mutasi sukses login via Biometric

1. Selesaikan login biometrik mobile yang memicu MFA hingga verifikasi faktor-2 sukses
2. Buka `Global Settings > Activity Log > Session`
3. Verifikasi baris log tercatat dengan Activity `Login`, Status `Success`, dan Note `Login with biometric`

### Verifikasi aktivitas yang TIDAK dicatat di log (Whitelist Policy)

4. Jalankan aksi-aksi berikut dan verifikasi TIDAK ADA baris log baru yang ditambahkan di kedua surface log:
   - Aktivasi pendaftaran Enrollment Authenticator yang berhasil maupun gagal
   - Pengiriman ulang kode via button [Resend code]
   - Navigasi tombol [Use a different method] / kembali ke Choose Verification Method
   - Pengiriman notifikasi email alert unusual login
   - Hangusnya sesi pre-auth karena TTL 10 menit terlewati
   - Pemblokiran aksi karena akun dinonaktifkan atau dihapus admin saat form terbuka
   - Kegagalan teknis server 5xx atau timeout jaringan

### Verifikasi kelengkapan kolom simetris pada kedua surface log

5. Buka `Global Settings > Activity Log > Session`
6. Verifikasi kolom entri log memuat: Date, User, Employee ID, Position, Division, Activity ("Login"), Status, Note, dan IP Address
7. Buka `Global Settings > User > Detail > User Log` untuk user bersangkutan
8. Verifikasi kolom entri log memuat: Date, Activity, Status, Note, dan IP Address (simetris 1:1)

### Integritas IP Address: Mengambil IP publik paling kiri dari X-Forwarded-For

9. Konfigurasikan proxy hop dengan header `X-Forwarded-For: 203.0.113.195, 70.41.3.18, 150.172.238.178`
10. Lakukan login dan selesaikan verifikasi faktor-2
11. Buka audit log dan periksa kolom IP Address
12. Verifikasi nilai IP Address yang dicatat adalah `203.0.113.195` (IP klien asli paling kiri)

## Notes

- Sesuai `auth-foundation.md` §10, proses enrollment dan aksi UI resend tidak dicatat ke surface audit log.
- IP Address diekstraksi dari alamat paling kiri header `X-Forwarded-For` pada proxy hop terpercaya.
