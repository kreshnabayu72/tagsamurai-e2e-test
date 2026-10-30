---
id: TC-GS-ROLE-E2E-034-assign-read-only-screening-popup-validasi-sukses-dan-klik-ganda
title: "Assign Read Only: Screening Popup, Validasi, Sukses, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-78
  - TC-GS-ROLE-79
  - TC-GS-ROLE-80
  - TC-GS-ROLE-82
coverage:
  web: automated
---

# Assign Read Only: Screening Popup, Validasi, Sukses, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Spec tidak berganti akun.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Read Only.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-034`; diubah dan dipulihkan sesuai catatan "Reset Pre-setup per TC" di `tc-role.md`):
  - Rahmat Hidayat (Pre-setup #11, Active): tanpa access level, punya baris Manage files (R,D); di-assign Read Only di TC-GS-ROLE-80 (Tabel Dinamis #4).
  - Wawan Setiawan (Pre-setup #11, Active): state kandidat (tanpa access level, tanpa baris role); di-assign Read Only di TC-GS-ROLE-82.
  - Hendra Wijaya (Pre-setup #5) hanya diamati di pool; tidak diubah. Ahmad Fauzi, Budi Santoso, Dewi Lestari (Total Control), dan Rina Putri (Read Only) hanya diamati di pool; tidak diubah.
- Pemulihan di hook `after`: Rahmat Hidayat kembali tanpa access level dengan baris role seperti Pre-setup (hanya Manage files R,D; baris Manage user and role hasil assign dihapus); Wawan Setiawan kembali ke state kandidat.
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): mengatur access level dan baris role user Pre-setup lewat API untuk Given dan pemulihan; membaca jumlah entry Modal Changelog dari UI.

Tabel Pool, nama yang dicari di picker Assign Read Only (TC-GS-ROLE-78):

| Nama | Hasil yang diharapkan |
|---|---|
| Rahmat Hidayat | baris tampil |
| Wawan Setiawan | baris tampil |
| Hendra Wijaya | baris tampil |
| Ahmad Fauzi | `No results found` tampil |
| Budi Santoso | `No results found` tampil |
| Dewi Lestari | `No results found` tampil |
| Rina Putri | `No results found` tampil |

## Test Steps

### TC-GS-ROLE-78: Screening Popup Assign Read Only dan pool-nya

1. Klik `[+ Assign]`
2. Verifikasi Title popup `Assign Read Only` tampil
3. Verifikasi toolbar `Search | Filter` tampil dengan placeholder Search `Search...`
4. Verifikasi kolom tabel picker `Checkbox | Name | Email | Position | Division | Status`
5. Verifikasi footer memuat pagination picker sendiri
6. Verifikasi footer memuat `[Cancel]` dan `[Assign]` dengan `[Assign]` enabled walau 0 terpilih

Untuk setiap baris Tabel Pool (langkah 7 sampai 8):

7. Ketik Search `<nama>`, tekan Enter
8. Verifikasi hasil pada kolom "Hasil yang diharapkan" tampil

9. Klik `(←)` pada kotak Search

### TC-GS-ROLE-79: Submit Assign Read Only tanpa memilih user

10. Klik `[Assign]`
11. Verifikasi teks error inline `You must pick a user` (danger) tampil di atas tombol footer
12. Verifikasi popup `Assign Read Only` tetap terbuka
13. Verifikasi tidak ada toast yang tampil

### TC-GS-ROLE-80: Assign Read Only ke user

14. Centang Rahmat Hidayat
15. Klik `[Assign]`
16. Verifikasi toast sukses `Success, Read Only has been assigned.` tampil
17. Verifikasi baris Rahmat Hidayat tampil di Tab Read Only
18. Verifikasi kolom Modified By baris Rahmat Hidayat bernilai `Ahmad F`
19. Buka Tab System
20. Buka Detail "Manage files"
21. Verifikasi baris Rahmat Hidayat: Read checked
22. Verifikasi baris Rahmat Hidayat: Delete unchecked
23. Buka Tab System
24. Buka Detail "Manage user and role"
25. Verifikasi baris baru Rahmat Hidayat: Read checked
26. Verifikasi baris Rahmat Hidayat: Create, Update, dan Delete unchecked
27. Buka Tab Read Only

### TC-GS-ROLE-82: Klik ganda [Assign] Popup Assign Read Only

28. Tunggu toast lama hilang otomatis
29. Buka Modal Changelog Tab Read Only
30. Catat jumlah entry Assign untuk Wawan Setiawan sebagai baseline
31. Tutup Modal Changelog
32. Klik `[+ Assign]`
33. Centang Wawan Setiawan
34. Klik `[Assign]` dua kali cepat
35. Verifikasi satu toast sukses `Success, Read Only has been assigned.` tampil
36. Buka Modal Changelog Tab Read Only
37. Verifikasi jumlah entry Assign untuk Wawan Setiawan bertambah tepat 1 dari baseline pada langkah 30
38. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional (satu topik aksi, Assign Read Only, pada Tab Read Only).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (38 langkah nominal, sekitar 50 dengan ekspansi perulangan langkah 7 sampai 8 untuk tujuh baris Tabel Pool). Alasan: empat TC satu topik aksi, layar, dan akun yang sama; urutan screening, validasi diblokir, aksi sukses, lalu klik ganda mengikuti bagian 3 konvensi; ekspansi berasal dari kewajiban Expected TC-GS-ROLE-78 b dan c memeriksa tujuh nama di pool. Blok klik ganda memakai popup baru dan user target sendiri (Wawan Setiawan), sehingga kegagalan blok sebelumnya tidak membuat blok itu kehilangan makna.
- Langkah 1 TC-GS-ROLE-79 dan TC-GS-ROLE-80 ("Klik [+ Assign]") memakai popup yang sama dengan TC-GS-ROLE-78 (tidak dibuka ulang; Search dibersihkan pada langkah 9), karena ketiga TC dimulai dari popup yang sama; satu popup dibuka untuk screening, validasi kosong, dan assign sukses (bagian 3 prinsip 6 dan 8).
- Tabel Pool memuat baris tampil lebih dahulu sebagai anchor positif sebelum baris `No results found` (bagian 8b butir 2); `No results found` pada hasil pencarian satu nama adalah anchor sah bagi absence nama itu di pool. Urutan Expected TC-GS-ROLE-78 (b tidak tampil, c tampil) dibalik untuk alasan ini.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik `(←)` pada kotak Search (langkah 9), membuka Tab System dan Tab Read Only (langkah 19, 23, 27), menunggu toast lama hilang (langkah 28), serta mencatat baseline dan membuka atau menutup Modal Changelog (langkah 29 sampai 31, 36, 38).
- Langkah 13 (tidak ada toast) didahului teks error inline pada langkah 11 sebagai anchor positif bahwa klik `[Assign]` sudah diproses.
- Perulangan langkah 7 sampai 8 memakai Tabel Pool di Prerequisites; parameter tiap iterasi hanya nama dan hasil yang diharapkan.
- Temuan untuk QA:
  - TC-GS-ROLE-78 menyebut "toolbar, kolom, footer sama dengan Popup Assign Total Control" tanpa daftar; spec mengacu ke Expected TC-GS-ROLE-51 (toolbar `Search | Filter` dengan placeholder `Search...`, kolom `Checkbox | Name | Email | Position | Division | Status`, footer pagination picker sendiri, `[Cancel]` dan `[Assign]`).
  - TC-GS-ROLE-80 dan TC-GS-ROLE-82 menyebut "Centang <nama>" tanpa cara menemukan baris bila picker lebih dari satu halaman; mekanisme menemukan baris diputuskan di tahap script.
  - Post Condition TC-GS-ROLE-80 tanpa langkah observasi dan tidak diasersi: (a) access level Rahmat Hidayat = Read Only (hanya diamati lewat Tab Read Only), (b) log Assign Read Only tercatat (Section 5).
  - TC-GS-ROLE-80 tidak menyebut pemulihan Rahmat Hidayat; Tabel Dinamis #4 menyatakan di-Remove di TC-GS-ROLE-88. Spec memulihkannya di hook `after`.
