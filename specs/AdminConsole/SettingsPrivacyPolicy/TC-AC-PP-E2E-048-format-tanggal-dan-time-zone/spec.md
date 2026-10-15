---
id: TC-AC-PP-E2E-048-format-tanggal-dan-time-zone
title: "Published At Mengikuti Date Format, Time Zone, dan Time Format General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-166
  - TC-AC-PP-167
  - TC-AC-PP-168
  - TC-AC-PP-210
coverage:
  web: automated
---

# Published At Mengikuti Date Format, Time Zone, dan Time Format General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Akun ini harus bisa mengubah General Settings.
- Dataset: Riwayat A, dengan Version 3 diterbitkan 10 Aug 2026 pukul 20:30 UTC (John Doe, Active), Version 2 (02 Jul 2026, John Doe), Version 1 (15 Jan 2026, Jane Smith). Hook `before` men-seed Riwayat A lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI).
- State global yang diubah spec ini: General Settings (Date Format `dd/MM/yy` dan `dd MMM yy`, Time Zone `Asia/Jakarta` (UTC+07:00) dan `America/New_York`, Time Format 12-hour). Nilai awal: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Pemulihan nilai awal dilakukan di akhir TC-168 dan TC-210 (langkah eksplisit) dan di hook `after` yang tetap jalan walau spec gagal di tengah.
- Kemampuan teknis: mengubah General Settings (lewat halaman General Settings Global Settings atau Fixture BE); membaca file CSV yang terunduh (TC-167 dan TC-210, kelas f). Jam server dan jam browser tidak diatur di spec ini.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state global General Settings yang memengaruhi seluruh spec lain dalam suite.
- Konfigurasi kolom tabel di cache browser dalam keadaan default (tidak diubah spec ini).
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-166: Kolom Published At dan info bar Modal View mengikuti Date Format General Settings

1. Atur Date Format General Settings menjadi `dd/MM/yy`
2. Buka Settings > Privacy Policy lewat sidebar
3. Verifikasi sel Published At baris `Version 3` bernilai `10/08/26`
4. Verifikasi sel Published At hanya menampilkan tanggal tanpa bagian jam
5. Klik teks tautan `Version 3`
6. Verifikasi info bar Modal View menampilkan `Published At 10/08/26`
7. Verifikasi info bar hanya menampilkan tanggal tanpa bagian jam
8. Klik `[✕]` di header modal
9. Atur Date Format General Settings menjadi `dd MMM yy`
10. Buka Settings > Privacy Policy lewat sidebar
11. Verifikasi sel Published At baris `Version 3` bernilai `10 Aug 26`
12. Klik teks tautan `Version 3`
13. Verifikasi info bar Modal View menampilkan `Published At 10 Aug 26`
14. Klik `[✕]` di header modal

### TC-AC-PP-167: Kolom Published At pada file export mengikuti Date Format General Settings

15. Atur Date Format General Settings menjadi `dd/MM/yy`
16. Buka Settings > Privacy Policy lewat sidebar
17. Klik icon Download
18. Pilih "Download as CSV"
19. Buka file yang terunduh
20. Verifikasi sel Published At baris `Version 3` bernilai `10/08/26`
21. Atur Date Format General Settings menjadi `dd MMM yy`

### TC-AC-PP-168: Time Zone General Settings menentukan tanggal Published At yang tampil pada batas hari, Time Format tidak berpengaruh

22. Atur Time Zone General Settings menjadi Asia/Jakarta (UTC+07:00)
23. Buka Settings > Privacy Policy lewat sidebar
24. Verifikasi sel Published At baris `Version 3` bernilai `11 Aug 26`
25. Klik teks tautan `Version 3`
26. Verifikasi info bar menampilkan `Published At 11 Aug 26`
27. Klik `[✕]` di header modal
28. Atur Time Zone General Settings menjadi America/New_York
29. Buka Settings > Privacy Policy lewat sidebar
30. Verifikasi sel Published At baris `Version 3` bernilai `10 Aug 26`
31. Atur Time Format General Settings menjadi 12-hour
32. Buka Settings > Privacy Policy lewat sidebar
33. Verifikasi sel Published At baris `Version 3` tidak berubah (`10 Aug 26`)
34. Verifikasi sel Published At tidak menampilkan jam
35. Atur Time Zone General Settings kembali ke UTC dan Time Format kembali ke 24-hour

### TC-AC-PP-210: Rentang filter Published At dan tanggal pada file export mengikuti Time Zone General Settings, bukan UTC

36. Atur Time Zone General Settings menjadi Asia/Jakarta (UTC+07:00)
37. Buka Settings > Privacy Policy lewat sidebar
38. Verifikasi sel Published At baris `Version 3` bernilai `11 Aug 26`
39. Buka panel Filter, pilih `Published At` 11 Aug 26 sampai 11 Aug 26, lalu klik `[Apply]`
40. Verifikasi tabel menampilkan `Version 3`
41. Verifikasi footer menampilkan `1–1 of 1`
42. Ubah rentang `Published At` menjadi 10 Aug 26 sampai 10 Aug 26, lalu klik `[Apply]`
43. Verifikasi tidak ada baris yang cocok; tabel menampilkan Title "No results found"
44. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
45. Klik `[Clear Field]` lalu klik `[Apply]`
46. Klik icon Download
47. Pilih "Download as CSV"
48. Buka file yang terunduh
49. Verifikasi sel Published At baris `Version 3` pada file bernilai `11 Aug 26`
50. Atur Time Zone General Settings kembali ke UTC

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini mengubah state global General Settings; seluruh perubahan dipulihkan di langkah 35 dan 50 (Post Condition TC-166 dan TC-168 menyatakan nilai dikembalikan) dan di hook `after` sebagai cadangan.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 8, 14, 27 (tutup Modal View), langkah 9 (kembalikan Date Format sebelum membuka halaman lagi, sesuai langkah 3 TC-166 yang mengulang dengan `dd MMM yy`), langkah 21 (kembalikan Date Format), langkah 35 dan 50 (pulihkan Time Zone dan Time Format), langkah 45 (bersihkan Filter).
- Langkah 22 sampai 35 (TC-168) memakai Date Format `dd MMM yy` dan Time Zone UTC sebagai nilai awal sesuai precondition TC.
- Langkah 4, 7, 34 mengasersi "tidak ada bagian jam" (Expected c TC-166 dan Expected c TC-168) sebagai klausa terpisah.
- Spec tidak membuat data selain mengubah General Settings; versi Privacy Policy tidak diubah.
- Temuan untuk QA: tidak ada.
- Panjang spec (50 langkah) melewati perkiraan 35 langkah. Alasan: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
