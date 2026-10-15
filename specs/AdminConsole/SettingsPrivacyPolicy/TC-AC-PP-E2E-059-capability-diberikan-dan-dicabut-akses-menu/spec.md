---
id: TC-AC-PP-E2E-059-capability-diberikan-dan-dicabut-akses-menu
title: "Pemberian dan Pencabutan Capability Manage Privacy Policy Mengubah Akses Menu"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-169
coverage:
  web: automated
---

# Pemberian dan Pencabutan Capability Manage Privacy Policy Mengubah Akses Menu

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai (tidak ada password di spec atau fixture; nama env `AC_MAYA_PASSWORD` dan `AC_TC_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; selain `AC_TC_PASSWORD`, nama itu belum terdaftar):

| TC | Peran dalam spec | Email | Env var password |
|---|---|---|---|
| TC-AC-PP-169 | User subjek Maya Putri (Principal, mula-mula tanpa Global Role "Manage privacy policy") | `mayaputri@qwertysystem.net` | `Spectra.env.AC_MAYA_PASSWORD` |
| TC-AC-PP-169 | Administrator Total Control yang mengatur role | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Hook `before`: men-seed dataset Riwayat A (Version 3 Active, 3 baris) lewat Fixture BE, memastikan Maya Putri tanpa Global Role "Manage privacy policy", lalu login sebagai Maya Putri (akun aktor pertama). Hook `after` (tetap jalan walau spec gagal di tengah): mencabut Global Role "Manage privacy policy" dari Maya Putri bila masih terpasang, mengembalikan dataset ke Riwayat A, dan mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat dan memastikan kondisi awal Global Role Maya Putri. Pemberian dan pencabutan Global Role oleh administrator dilakukan di UI Admin Console sebagai Total Control.
- Suite berjalan serial (`parallel: false`) karena spec mengubah capability (Global Role) dan dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-169: Memberi dan mencabut capability Manage privacy policy mengubah akses menu Privacy Policy

1. Buka grup Settings pada sidebar sebagai Maya Putri (login di hook `before`)
2. Verifikasi item "Privacy Policy" tidak tampil
3. Logout
4. Login sebagai administrator Total Control
5. Berikan Global Role "Manage privacy policy" (Read dan Update) kepada Maya Putri
6. Logout
7. Login ulang sebagai Maya Putri
8. Buka grup Settings pada sidebar
9. Verifikasi item "Privacy Policy" tampil
10. Klik "Privacy Policy"
11. Verifikasi halaman Privacy Policy terbuka
12. Klik `[⋯]` pada baris `Version 3`
13. Verifikasi opsi `Edit` tersedia di dropdown
14. Pilih `Edit`
15. Tunggu konten termuat
16. Verifikasi tombol `[Publish New Version]` tersedia
17. Klik `[✕]` pada header modal
18. Logout
19. Login sebagai administrator Total Control
20. Cabut Global Role "Manage privacy policy" dari Maya Putri
21. Logout
22. Login ulang sebagai Maya Putri
23. Buka grup Settings pada sidebar
24. Verifikasi item "Privacy Policy" kembali tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Dipisah dari TC-AC-PP-84 (spec `TC-AC-PP-E2E-014-capability-dicabut-saat-aksi-berjalan`) karena dua keluarga akun dan gabungan keduanya melewati batas ukuran spec (bagian 3, S-10).
- Tiap ganti akun punya langkah logout dan login eksplisit (S-07); login akun aktor pertama (Maya Putri) ada di hook `before`.
- Langkah penghubung (S-03): langkah 12-15 (membuka dropdown, memilih `Edit`, menunggu konten termuat) adalah jalur menuju langkah 16 yang menurunkan Expected b ("`Edit` dan `Publish New Version` tersedia"); langkah 17 menutup modal Edit yang bersih tanpa dialog.
- Temuan untuk QA: (1) TC-AC-PP-169 langkah 2 dan 4 tidak menyebut lokasi UI pengaturan Global Role (mis. Settings > User atau Settings > Role); tim FE menentukan jalurnya. (2) Expected b ("`Edit` dan `Publish New Version` tersedia") tidak punya langkah pemeriksaannya di TC; langkah 12-16 diturunkan dari Expected. (3) Post Condition ("Global Role Maya Putri kembali ke kondisi awal") tidak punya langkah observasi selain hook `after` sehingga tidak diasersi.
