---
id: TC-AUTH-OTP-E2E-049-duplikasi-tab-konfirmasi-token-sekali-pakai
title: "Duplikasi Tab pada Layar Confirm to Continue: Konfirmasi Kedua dengan Token yang Sama Ditolak"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-110
coverage:
  web: automated
---

# Duplikasi Tab pada Layar Confirm to Continue: Konfirmasi Kedua dengan Token yang Sama Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata; sesi, token, dan log dibuktikan lewat perilaku UI dan log Global Settings).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu. Hook `after` mengembalikan sesi admin ke akun default suite.
- Hook `before` (seeding API) membuat user profil POLICY berikut (Activated, Active ON; sudah login sukses dalam 30 hari terakhir pada device dikenali; Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu) dengan suffix per run `+{runId}-049`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-110: `Yoga Halim` (`yogahalim+{runId}-049@qwertysystem.net`)
- Baseline log: hook `before` mencatat jumlah baris `Yoga Halim` di `Global Settings > Activity Log > Session` dan di `Global Settings > User > Detail > User Log`; "tepat satu baris baru" pada langkah 15 dan 17 dihitung terhadap baseline itu (S-12).
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP; duplikasi tab pada layar Confirm to Continue sehingga tab B memegang token pra-autentikasi yang sama dengan tab A dalam satu jendela privat; Principal dengan hak publish Privacy Policy sehingga versi baru sudah terpublikasi sebelum profil POLICY dipakai; dua konteks browser (browser admin dan jendela privat publik); reCAPTCHA mode uji.
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru sebelum `Yoga Halim` di-seed (hook `before`). Versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-110: Konfirmasi kedua dengan token pra-autentikasi yang sama setelah konfirmasi sukses ditolak

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `yogahalim+{runId}-049@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Centang checkbox "I have read and agree to the Privacy Policy *"
7. Duplikasi tab pada layar Confirm to Continue sebelum Continue (tab B memegang token yang sama)
8. Pada tab A klik button [Continue ➔]
9. Verifikasi tab A: browser dialihkan ke Portal — Product Hub
10. Verifikasi tab A: sesi aktif untuk `Yoga Halim`
11. Pada tab B klik button [Continue ➔]
12. Verifikasi tab B: konfirmasi ditolak server karena token sekali pakai sudah terpakai
13. Verifikasi tab B: browser kembali ke halaman `Auth > Login with Password`
14. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan cari entri untuk `Yoga Halim`
15. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Success `Login with OTP` untuk `Yoga Halim` di `Global Settings > Activity Log > Session` (satu sesi)
16. Buka `Global Settings > User > Detail > User Log` untuk `Yoga Halim`
17. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Success `Login with OTP` di `Global Settings > User > Detail > User Log`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness c (multi-konteks): tab B adalah objek asersi (perilaku tab B setelah tab A berhasil), bukan pemicu, sehingga pengecualian P-2 tidak berlaku dan TC-AUTH-OTP-110 dipisah dari spec `TC-AUTH-OTP-E2E-032-agreement-gate-policy-baru-dan-konfirmasi-sukses` ke spec ini. Spec ini hanya memuat satu TC; duplikasi tab hanya satu kali dan tidak memerlukan harness multi-browser.
- Langkah 14 adalah langkah penghubung ganti konteks ke browser admin (S-03, S-07). Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-AUTH-OTP-110 Expected c ("Di surface log hanya satu baris Success") tidak menyebut surface mana; TC sumber juga tidak punya langkah membuka log. Spec menambah langkah 14 sampai 17 yang memeriksa kedua surface (Activity Log Session dan User Log) dengan baseline. Mohon QA menambah langkah pemeriksaan log di TC.
  - TC-AUTH-OTP-110 langkah 7 menyebut "Duplikasi tab" tanpa menyebut cara duplikasi dan bahwa kedua tab berbagi jendela privat yang sama; spec mengasumsikan keduanya berada di konteks browser yang sama (kebutuhan dicatat di Prerequisites).
