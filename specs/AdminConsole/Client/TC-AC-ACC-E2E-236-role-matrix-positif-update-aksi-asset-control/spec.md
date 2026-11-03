---
id: TC-AC-ACC-E2E-236-role-matrix-positif-update-aksi-asset-control
title: "Role Matrix Positif: Pemegang Update Manage Active Client Menjalankan Generate Enrollment QR, Revoke Tablet, dan Deactivate Station"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-614
  - TC-AC-ACC-615
  - TC-AC-ACC-616
coverage:
  web: automated
---

# Role Matrix Positif: Pemegang Update Manage Active Client Menjalankan Generate Enrollment QR, Revoke Tablet, dan Deactivate Station

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec positif, bagian 3a konvensi): satu role spesifik yang berhak atas aksi, langkahnya identik untuk semua TC.

| Role | Akun | Env password | Assignment |
|---|---|---|---|
| Active-Update-Only A-06 (Manage active client: Update + Read) | `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script) | Hanya node Area Jakarta (exact-match) |

- Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (skrip seed, bukan lewat UI; di-seed ulang lewat reset data uji karena Deactivate dan Revoke permanen): C-ROL-12 "PT Stasiun Uji" (Active; Asset Control Total 4 / Used 2 / Available 2; Station "Gerbang Uji A" Active dengan Tablet "Tablet Uji A1" dan "Tablet Uji A2"; Station "Gerbang Uji B" Active dengan Tablet "Tablet Uji B1"; SFR Asset Control "Reader Uji" tanpa station aktif).
- Kemampuan teknis: jam server uji dapat dimajukan (token Active hasil TC-AC-ACC-614 dikembalikan ke Expired dengan memajukan jam server 15 menit di hook `after`; jam dipulihkan).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- State global: jam server dimajukan lalu dipulihkan di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_CLIENT_ACTIVE_UPDATE_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Stasiun Uji" di List Client, tekan Enter, klik Company Name "PT Stasiun Uji", lalu klik Tab Asset Control

### TC-AC-ACC-614: Generate Enrollment QR oleh pemegang Update

2. Klik [Generate Enrollment QR]
3. Verifikasi dialog Title "Enrollment QR" tampil dengan QR Code, dropdown "Select Smart Fixed Reader" terisi "Reader Uji" tanpa dipilih manual
4. Verifikasi dialog memuat teks "Scan this QR to enroll a tablet as an Asset Control station."
5. Verifikasi dialog memuat teks "This QR can only be used once and expires in 15 minutes."
6. Verifikasi tidak ada toast sukses
7. Klik [Close]

### TC-AC-ACC-616: Revoke Tablet oleh pemegang Update

8. Klik row Station "Gerbang Uji B" untuk expand Tablet List
9. Buka ⋯ baris Tablet "Tablet Uji B1" lalu klik Revoke
10. Verifikasi dialog: Title "Revoke Tablet", bullet `• Tablet Uji B1`, teks "This will revoke this tablet's enrollment. It will no longer sync with this station. Are you sure you want to revoke it?", tombol [Cancel] dan [Revoke]
11. Klik [Revoke] pada dialog
12. Verifikasi toast sukses: "Success, tablet has been revoked."
13. Verifikasi Tablet "Tablet Uji B1" berstatus Revoked

### TC-AC-ACC-615: Deactivate Station oleh pemegang Update

14. Buka ⋯ baris Station "Gerbang Uji A" lalu klik Deactivate
15. Verifikasi dialog: Title "Deactivate Station", bullet `• Gerbang Uji A`, teks "This will deactivate this station and revoke all of its tablets. Its Enrollment QR slot will return to available quota. Are you sure you want to deactivate it?", tombol [Cancel] dan [Deactivate]
16. Klik [Deactivate] pada dialog
17. Verifikasi toast sukses: "Success, station has been deactivated."
18. Klik row Station "Gerbang Uji A" untuk expand Tablet List
19. Verifikasi Station "Gerbang Uji A" berstatus Deactivated
20. Verifikasi "Tablet Uji A1" dan "Tablet Uji A2" berstatus Revoked
21. Verifikasi Station Quota: Total 4, Used 1, Available 3

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 7 (menutup dialog Enrollment QR), langkah 8 dan 18 (expand row agar Tablet List teramati).
- Urutan TC di spec (614, 616, 615) berbeda dari urutan nomor TC agar aksi yang menghabisi data (Deactivate Station) berada paling akhir (prinsip 3 butir 5); tiap TC memakai Station yang berbeda sehingga nilai kuota TC-AC-ACC-615 (Used 2 menjadi 1) tetap sesuai Expected.
- Kombinasi role x aksi lain (Read-saja, Create-saja, Delete-saja) tidak punya TC sumber untuk aksi Asset Control di slice ini; spec negatif Read ada di spec 237.
- Temuan untuk QA:
  - TC-AC-ACC-614 sampai TC-AC-ACC-616 menyebut Post Condition seed ulang C-ROL-12 tanpa menyebut token Active hasil TC-AC-ACC-614; spec memulihkannya lewat memajukan jam server di hook `after`.
