---
id: TC-GS-IMPORT-E2E-116-ai-field-shortening-tanpa-badge-untuk-field-di-luar-daftar-dan-tanpa
title: "AI Field Shortening: tanpa badge untuk field di luar daftar dan tanpa saran memadai; respons dalam batas waktu tetap bersaran"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-299
  - TC-GS-IMPORT-300
  - TC-GS-IMPORT-698
  - TC-GS-IMPORT-699
  - TC-GS-IMPORT-703
  - TC-GS-IMPORT-866
coverage:
  web: automated
---

# AI Field Shortening: tanpa badge untuk field di luar daftar dan tanpa saran memadai; respons dalam batas waktu tetap bersaran

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Tab Brand); perpindahan Tab berikutnya ditulis sebagai langkah penghubung.
- Kondisi awal tiap TC (Kontrak Fixture R1): Client C tanpa draft pada Tab yang diuji. Skrip reset draft Client C disediakan tim FE/BE dan dijalankan di hook `before` serta sebagai langkah penghubung sebelum tiap TC; mekanismenya tidak ada di TC (lihat Temuan untuk QA).
- Layanan AI: mock deterministik (Data Dinamis D-11, D-40, tabel D-41 dan D-42) yang diatur tim QA/BE lewat hook uji di lingkungan non-produksi. Mode diubah di langkah kasus (bukan di hook): mode kosong (TC 299), mode normal (TC 300, 698, 699), dan mode tunda 3 detik (TC 703, 866). Hook `after` mengembalikan mode ke normal.
- Jeda nyata: satu langkah "Tunggu 4 detik" pada TC 703 (jeda pendek di bawah ±30 detik; mock menunda respons 3 detik sehingga jam server tidak dimanipulasi).
- Data Dinamis (berkas upload disediakan tim QA; fixture baru `Fixture.import.aiFieldShorteningNegative116`; berkas statis tanpa suffix per run karena draft direset per TC):

| TC | Tab | Berkas | Isi data | Mode mock AI |
|---|---|---|---|---|
| 299 | Brand | `ai-brand-long.csv` (D-44) | Brand Name = nilai sumber Brand pada D-41 (121 karakter) | kosong |
| 300 | Measurement | `measurement-symbol-11.csv` | Unit Name `Gram per Liter`, Symbol `abcdefghijk` (11 karakter) | normal |
| 698 | User Login | `ai-ul-empid-long.csv` (berkas User Login standar D-45 ditambah kolom `Employee ID`) | Siti Rahmawati, Email `siti.rahmawati@example.com`, Division `Engineering`, Position kosong, Employee ID `EMP-` diikuti angka berulang sampai 121 karakter | normal |
| 699 | Division | `ai-division-code-16.csv` (D-44) | Division Name `Logistik Pusat`, Code `ABCDEFGHIJKLMNOP` (16 karakter) | normal |
| 703 | Brand | `ai-brand-long.csv` (D-44) | Brand Name = nilai sumber Brand pada D-41 (121 karakter) | tunda 3 detik |
| 866 | Brand | `ai-brand-long-2.csv` | baris 1 nilai sumber Brand pertama D-41 (121 karakter), baris 2 nilai sumber Brand kedua D-41 (125 karakter) | tunda 3 detik |

- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft Client C pada semua Tab yang disentuh spec ini dan kembalikan mock AI ke mode normal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: input upload berkas; mock layanan AI dengan mode kosong, normal, dan tunda 3 detik (D-40); skrip reset draft (Kontrak Fixture R1) disediakan tim FE/BE.
- State global: mock layanan AI (dikembalikan ke normal di hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-IMPORT-299: Tanpa saran memadai (mode kosong), tidak ada badge

1. Atur mock layanan AI ke mode kosong (D-40)
2. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi baris #1 berstatus `error`
5. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters"
6. Verifikasi Error Summary Callout menampilkan badge "1 row"
7. Verifikasi sel Brand Name baris #1 tidak menampilkan badge saran (anchor: baris #1 `error` dan Callout sudah tampil pada langkah 4 sampai 6)

### TC-GS-IMPORT-300: Field Symbol di luar daftar tidak memakai AI Field Shortening

8. Atur mock layanan AI ke mode normal (D-40); reset draft Client C pada Tab Brand lewat skrip reset; buka Tab Measurement
9. Klik [Upload File] di toolbar dan pilih berkas `measurement-symbol-11.csv`
10. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
11. Verifikasi baris #1 berstatus `error`
12. Verifikasi Error Summary Callout memuat "Symbol: Max. 10 characters"
13. Verifikasi Error Summary Callout menampilkan badge "1 row"
14. Verifikasi sel Symbol baris #1 tidak menampilkan badge saran
15. Verifikasi sel Unit Name baris #1 tidak menampilkan badge saran

### TC-GS-IMPORT-698: Field Employee ID di luar daftar tidak memakai AI Field Shortening

16. Reset draft Client C pada Tab Measurement lewat skrip reset; buka Tab User Login
17. Klik [Upload File] di toolbar dan pilih berkas `ai-ul-empid-long.csv`
18. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
19. Verifikasi baris #1 berstatus `error`
20. Verifikasi Error Summary Callout memuat "Employee ID: Max. 120 characters"
21. Verifikasi Error Summary Callout menampilkan badge "1 row"
22. Verifikasi sel Employee ID baris #1 tidak menampilkan badge saran

### TC-GS-IMPORT-699: Field Code Division di luar daftar tidak memakai AI Field Shortening

23. Reset draft Client C pada Tab User Login lewat skrip reset; buka Tab Division
24. Klik [Upload File] di toolbar dan pilih berkas `ai-division-code-16.csv`
25. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
26. Verifikasi baris #1 berstatus `error`
27. Verifikasi Error Summary Callout memuat "Code: Max. 15 characters"
28. Verifikasi Error Summary Callout menampilkan badge "1 row"
29. Verifikasi sel Code baris #1 tidak menampilkan badge saran

### TC-GS-IMPORT-703: Respons AI dalam 3 detik tetap menampilkan badge saran

30. Reset draft Client C pada Tab Division lewat skrip reset; buka Tab Brand; atur mock layanan AI ke mode tunda 3 detik (D-40)
31. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
32. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
33. Tunggu 4 detik
34. Verifikasi sel Brand Name baris #1 menampilkan badge inline "AI suggestion: 'Samsung Electronics Indonesia'?" disertai `[Accept]` dan `[Dismiss]`
35. Verifikasi baris #1 tetap `error`

### TC-GS-IMPORT-866: Batas 5 detik per permintaan saran, dua sel keduanya bersaran

36. Reset draft Client C pada Tab Brand lewat skrip reset (mock tetap mode tunda 3 detik)
37. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long-2.csv`
38. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
39. Verifikasi modal Confirm Mapping tertutup
40. Verifikasi Staging Table menampilkan baris #1 dan #2 berstatus `error`
41. Tunggu sampai badge saran tampil (batas tunggu 15 detik)
42. Verifikasi sel Brand Name baris #1 menampilkan badge "AI suggestion: 'Samsung Electronics Indonesia'?" disertai `[Accept]` dan `[Dismiss]`
43. Verifikasi sel Brand Name baris #2 menampilkan badge "AI suggestion: 'Lenovo Technology Indonesia'?" disertai `[Accept]` dan `[Dismiss]`
44. Verifikasi kedua sel mendapat saran karena batas 5 detik dihitung per permintaan dan permintaan per sel diajukan bersamaan (disimpulkan dari langkah 42 dan 43; tidak teramati terpisah)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan ID menjadi 299, 300, 698, 699, 703, 866 supaya mode mock AI hanya berubah tiga kali (kosong, normal, tunda 3 detik); tidak ada TC yang bergantung pada TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 16, 23, 30, dan 36 (atur mode mock, reset draft Client C, pindah Tab). Reset draft memenuhi Kontrak Fixture R1 sebelum tiap TC; langkah 33 dan 41 adalah jeda tunggu.
- Spec melewati sekitar 35 langkah (44 langkah). Alasan: keenam blok berdiri sendiri, memakai satu kelas harness (mock AI Field Shortening) dan satu akun; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tiap blok punya draft serta Tab sendiri.
- Mock AI mode kosong dan tunda 3 detik adalah kondisi UI yang diamati (tidak ada saran; saran terlambat), bukan kegagalan yang dipaksa pada API (kelas b); intercept tidak dipakai.
- Pembagian TC lintas spec: TC-GS-IMPORT-299 dan 300 melengkapi asersi badge pada spec 115 (badge tampil); kasus Accept dan Dismiss ada di spec 117.
- Temuan untuk QA:
  - TC 698 menulis Employee ID sebagai `EMP-` diikuti angka berulang 121 karakter; TC tidak memberi pola ulang yang pasti, spec memakai nilai dari TC apa adanya (121 karakter).
  - Skrip reset draft Client C (Kontrak Fixture R1) tidak didefinisikan di TC; disediakan tim FE/BE.
  - TC 866 Expected c ("permintaan per sel diajukan bersamaan") tidak punya cara observasi terpisah; hanya disimpulkan dari badge kedua sel (langkah 44).
  - Post Condition TC 299, 300, 698, 699, 703 ("Draft ... berisi 1 baris `error`") dan TC 866 ("mock dikembalikan ke mode normal") tidak punya langkah observasi di TC; tidak diasersi (S-01).
