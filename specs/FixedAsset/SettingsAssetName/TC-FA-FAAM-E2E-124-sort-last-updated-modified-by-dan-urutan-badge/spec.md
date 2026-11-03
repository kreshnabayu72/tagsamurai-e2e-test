---
id: TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge
title: "Sort: Last Updated, Modified By, Kolom Tanpa Sort, Urutan Badge, dan Tie-Breaker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-395
  - TC-FA-FAAM-396
  - TC-FA-FAAM-397
  - TC-FA-FAAM-398
  - TC-FA-FAAM-399
  - TC-FA-FAAM-400
  - TC-FA-FAAM-401
coverage:
  web: automated
---

# Sort: Last Updated, Modified By, Kolom Tanpa Sort, Urutan Badge, dan Tie-Breaker

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, model `3310`, `5420`, `7420`), `Service Vehicle` (Pre-setup #14, Default Addon `Maintenance`, `Tracking`, `Maps`), `Seed Item 01` sampai `Seed Item 30` (Total Asset 0). Modified By pada data: `David Kurniawan`, `Michael Wijaya`, `Sarah Johnson` (Pre-setup #28).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-395: Sort kelas Last Updated (tanggal): siklus tiga state
1. Klik header kolom Last Updated satu kali
2. Verifikasi klik 1 Ascending: `Oldest First`
3. Klik header kolom Last Updated kedua kali
4. Verifikasi klik 2 Descending: `Newest First`
5. Klik header kolom Last Updated ketiga kali
6. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z
### TC-FA-FAAM-396: Sort kelas Modified By (nama lengkap): siklus tiga state
7. Klik header kolom Modified By satu kali
8. Verifikasi klik 1 Ascending: A-Z menurut nama lengkap (`David Kurniawan`, `Michael Wijaya`, `Sarah Johnson`), bukan teks singkat
9. Klik header kolom Modified By kedua kali
10. Verifikasi klik 2 Descending: Z-A menurut nama lengkap
11. Klik header kolom Modified By ketiga kali
12. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z
### TC-FA-FAAM-397: Kolom Checkbox dan Actions tidak memiliki icon sort
13. Verifikasi header kolom Asset Name memiliki icon sort
14. Perhatikan header kolom Checkbox dan kolom Actions (⋯)
15. Verifikasi header kolom Checkbox dan Actions (⋯) tidak memiliki icon sort
### TC-FA-FAAM-398: Urutan badge di dalam satu sel tetap A-Z saat kolom di-sort descending
16. Klik header kolom Model/Type dua kali (Descending)
17. Verifikasi badge model di sel `Dell Latitude` tetap `3310`, `5420` (A-Z) walau baris di-sort Z-A
18. Klik header kolom Model/Type satu kali sampai kembali netral
### TC-FA-FAAM-399: Urutan badge Default Addon di sel tetap urutan enum saat sort descending
19. Klik header kolom Default Addon dua kali (Descending)
20. Verifikasi badge sel `Service Vehicle` tetap `Maintenance`, `Tracking` (urutan enum)
21. Verifikasi chip `+1 more` tampil pada sel `Service Vehicle`
22. Klik header kolom Default Addon satu kali sampai kembali netral
### TC-FA-FAAM-400: Nilai sort sama diurut deterministik menurut default sort tabel
23. Klik header kolom Total Asset (Ascending)
24. Verifikasi baris ber-Total Asset 0 pada halaman 1 (page size 10) berurutan menurut Asset Name A-Z
25. Klik halaman 2
26. Verifikasi baris ber-Total Asset 0 pada halaman 2 berurutan menurut Asset Name A-Z dan baris pertamanya melanjutkan tepat setelah baris terakhir halaman 1, tanpa baris ganda atau terlewat di batas halaman 1-2
27. Klik halaman 3
28. Verifikasi baris ber-Total Asset 0 pada halaman 3 berurutan menurut Asset Name A-Z dan baris pertamanya melanjutkan tepat setelah baris terakhir halaman 2, tanpa baris ganda atau terlewat di batas halaman 2-3
29. Klik header kolom Total Asset dua kali sampai kembali netral
### TC-FA-FAAM-401: Mengganti sort mempertahankan nomor halaman
30. Pindah ke halaman 2
31. Klik header kolom Code
32. Verifikasi tabel tetap di halaman 2
33. Verifikasi tabel memakai urutan dataset baru (sort Code Ascending)
34. Klik header kolom Code dua kali sampai kembali netral

## Notes

- Verifikasi icon sort pada header Asset Name (TC-FA-FAAM-397) adalah anchor positif untuk asersi absence pada header Checkbox dan Actions (bagian 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): mengembalikan sort ke netral di akhir tiap blok (S-09), berpindah ke halaman 2 dan 3 pada TC-FA-FAAM-400.
- TC-FA-FAAM-400 diamati antar halaman pada page size 10. Total Asset 0 dimiliki 30 `Seed Item` dan mungkin satu Asset Name contoh lain (namanya tidak tertulis di Pre-setup), sehingga asersi memakai urutan A-Z dan kontinuitas di batas halaman 1-2 dan 2-3, bukan pembagian nama per halaman.
