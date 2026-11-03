---
id: TC-FA-GRP-E2E-131-groups-list-mutasi-saat-terfilter-ter-search-dan-paginasi-kasus-tepi
title: "Groups List: Mutasi Saat Tabel Terfilter/Ter-Search (Create dan Rename) dan Paginasi Kasus Tepi (Halaman Tidak Valid, Hapus Baris Terakhir, Ganti Page Size/Sort)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-424
  - TC-FA-GRP-425
  - TC-FA-GRP-1134
coverage:
  web: automated
---

# Groups List: Mutasi Saat Tabel Terfilter/Ter-Search (Create dan Rename) dan Paginasi Kasus Tepi (Halaman Tidak Valid, Hapus Baris Terakhir, Ganti Page Size/Sort)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-131`, bagian 5), dibuat lewat API di `before` oleh akun aktor: group `Edit Target {runId}-131` (level 1, Assignable, kosong); group `Edge Parent {runId}-131` (level 1, Function None) dengan 11 child kosong Assignable `Edge 01 {runId}-131` sampai `Edge 11 {runId}-131` (halaman 1 = Edge 01 sampai Edge 10, halaman 2 = Edge 11). Dipakai sebagai pengganti `Edit Target` dan Head Office (11 child kosong) pada TC.
- Data baru yang dibuat langkah (dibersihkan di `after`): group `Filter None {runId}-131` (Function None, TC-FA-GRP-424) dan `Renamed X {runId}-131` (hasil rename `Edit Target {runId}-131`, TC-FA-GRP-425).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Edit Target {runId}-131`, `Renamed X {runId}-131`, `Filter None {runId}-131`, `Edge Parent {runId}-131` beserta child.

## Test Steps

### TC-FA-GRP-424: Create group yang tidak cocok filter

1. Klik icon Filter
2. Pilih `Assignable` pada dropdown Function
3. Klik [Apply]
4. Klik `[+] Group` pada sidebar Group Tree
5. Isi Group Name `Filter None {runId}-131` dan pilih Function `None`
6. Klik [Submit]
7. Verifikasi toast `Success, group has been created.` tampil
8. Verifikasi group `Filter None {runId}-131` tidak tampil pada tabel yang terfilter
9. Verifikasi group `Filter None {runId}-131` tampil pada sidebar Group Tree
10. Klik icon Filter
11. Klik [Clear Field]
12. Klik [Apply]

### TC-FA-GRP-425: Rename keluar dari keyword Search

13. Ketik Search `edit target {runId}-131`, tekan Enter
14. Verifikasi group `Edit Target {runId}-131` tampil pada hasil search
15. Klik row action `Edit` pada baris `Edit Target {runId}-131`
16. Ubah Group Name menjadi `Renamed X {runId}-131`
17. Klik [Save]
18. Verifikasi toast `Success, group has been updated.` tampil
19. Verifikasi group `Renamed X {runId}-131` tidak tampil pada hasil search
20. Klik `(←)` pada kotak Search

### TC-FA-GRP-1134: Kasus tepi paginasi

21. Klik `Edge Parent {runId}-131` di sidebar Group Tree
22. Ketik nomor halaman `0` pada input halaman, tekan Enter
23. Verifikasi halaman tidak berubah (input diabaikan): halaman 1 tetap aktif
24. Ketik nomor halaman `99` pada input halaman, tekan Enter
25. Verifikasi halaman tidak berubah (input diabaikan): halaman 1 tetap aktif
26. Ketik nomor halaman `abc` pada input halaman, tekan Enter
27. Verifikasi halaman tidak berubah (input diabaikan): halaman 1 tetap aktif
28. Pindah ke halaman 2 lewat pagination
29. Verifikasi halaman 2 hanya berisi baris `Edge 11 {runId}-131`
30. Klik header Group satu kali
31. Verifikasi tabel tetap berada di halaman yang sedang dibuka (halaman 2)
32. Klik row action `Delete` pada baris `Edge 11 {runId}-131`
33. Klik [Delete] pada dialog konfirmasi
34. Verifikasi tabel pindah ke halaman terakhir yang masih ada (halaman 1)
35. Ubah page size ke 25
36. Ubah page size kembali ke 10
37. Verifikasi tabel berada di halaman 1

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membersihkan filter dan Search antar TC, membuka node di sidebar, dan berpindah halaman (S-03, S-09, R-16). Toast `Success, group has been updated.` pada TC-FA-GRP-425 dipakai sebagai anchor positif asersi absence (bagian 8b butir 2); toast itu tidak ada pada Expected TC-FA-GRP-425.
- Aksi menghapus data (`Edge 11`) ditaruh paling akhir (S-10); `[+] Group` pada TC-FA-GRP-424 memakai Function `None` sesuai TC.
- Seluruh TC memakai data milik spec (`Edit Target`, `Edge Parent` dengan 11 child) sebagai pengganti Pre-setup tambahan (S-06).
- Spec 37 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Password akun aktor memakai env baru `FA_TC_PASSWORD`; perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
