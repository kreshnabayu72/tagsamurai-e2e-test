---
id: TC-FA-FAAL-E2E-049-isi-berkas-download-tab-user-action
title: "Isi Berkas Download Tab User Action: Sel, Format CSV dan XLSX, Urutan Baris dan Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-178
  - TC-FA-FAAL-179
  - TC-FA-FAAL-180
  - TC-FA-FAAL-181
  - TC-FA-FAAL-185
  - TC-FA-FAAL-186
  - TC-FA-FAAL-187
  - TC-FA-FAAL-188
coverage:
  web: automated
---

# Isi Berkas Download Tab User Action: Sel, Format CSV dan XLSX, Urutan Baris dan Kolom

## Prerequisites

- Mode: FE+BE (backend nyata; unduhan nyata tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka). Langkah 25 memakai akun Total Control di client Batas Waktu (ganti akun eksplisit) dengan password `Spectra.env.FA_TCBATAS_PASSWORD` (butir "Env var" di `suite.md`); hook `after` mengembalikan sesi ke akun default suite.
- General Settings staf akun aktor: Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (nilai default Pre-setup #1; TC-FA-FAAL-178 butir d).
- Data Pre-setup: Data Log Tab User Action UA-01 sampai UA-15 (#12), disediakan lewat seed suite; nilai sel yang diasersi berasal dari tabel Pre-setup #12 TC sumber. Client Batas Waktu (#15) dengan baris BD-U5 Name `Gedung "Utama", Lantai 1` untuk langkah 25 sampai 30; akun Total Control client itu tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE). Data Dinamis: tidak ada.
- Jendela Seed Tab User Action (precondition TC-FA-FAAL-187): Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15), diterapkan di langkah 14 sehingga baris data pertama berkas default adalah UA-01 dan Oldest First adalah UA-15 (hanya baris seed #12). TC-FA-FAAL-178 sampai 181, 185, 186, dan 188 tidak memuat Filter Date. Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Kemampuan teknis (disediakan tim FE): penangkap unduhan browser; parser CSV (nilai sel, header, byte awal, urutan baris) dan parser XLSX (daftar nama sheet).
- State yang diubah dan pemulihannya: urutan kolom Tab User Action lewat Setup Column (dipulihkan langkah 24; hook `after` menghapus preferensi kolom di browser sebagai cadangan, kemampuan disediakan tim FE) dan Sort Date (dikembalikan netral pada langkah 18).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan konfigurasi kolom) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### Satu unduhan CSV Tab User Action dibaca untuk TC-FA-FAAL-178 sampai 181

1. Klik tab User Action
2. Klik icon Download, pilih `Download as CSV`, lalu buka berkas dengan parser CSV

### TC-FA-FAAL-178: Sel Date

3. Verifikasi sel Date baris UA-01 bernilai `18/06/26, 14:30`
4. Verifikasi sel Date baris UA-15 bernilai `18/06/26, 07:30`

### TC-FA-FAAL-179: Sel Action, Object, Name, dan Field

5. Verifikasi baris UA-02: Action `Edit`, Object `Groups`, Name `Gedung A > Lantai 3 - Renovasi`, Field `Group Name`
6. Verifikasi sel Name baris UA-08 bernilai `-`

### TC-FA-FAAL-180: Sel Old Value dan New Value

7. Verifikasi baris UA-01: Old Value `-`, New Value `Total Control`
8. Verifikasi baris UA-03: Old Value `Electronic Devices`, New Value `-`

### TC-FA-FAAL-181: Sel Modified By

9. Verifikasi sel Modified By baris UA-01 bernilai `Admin Alpha`
10. Verifikasi sel Modified By baris UA-05 bernilai `Ahmad Dahlan`
11. Verifikasi sel Modified By baris UA-11 bernilai `System`

### TC-FA-FAAL-186: Format XLSX

12. Klik icon Download, pilih `Download as XLSX`, lalu buka berkas dengan parser XLSX
13. Verifikasi berkas memuat satu sheet bernama `Sheet1`
14. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-187: Urutan baris mengikuti Sort aktif

15. Klik header Date sekali (Oldest First)
16. Klik icon Download, pilih `Download as CSV`, lalu buka berkas
17. Verifikasi baris data pertama berkas adalah UA-15
18. Klik header Date dua kali lagi hingga netral
19. Klik icon Download, pilih `Download as CSV`, lalu buka berkas
20. Verifikasi baris data pertama berkas adalah UA-01 (default Date Newest First)

### TC-FA-FAAL-188: Urutan kolom berkas sama dengan urutan kolom tabel

21. Lewat Setup Column pindahkan Modified By ke posisi pertama, klik `[Save]`
22. Klik icon Download, pilih `Download as CSV`, lalu buka berkas
23. Verifikasi header berkas `Modified By, Date, Action, Object, Name, Field, Old Value, New Value`
24. Lewat Setup Column pindahkan Modified By kembali ke posisi terakhir, klik `[Save]`

### TC-FA-FAAL-185: Format CSV pada client Batas Waktu

25. Ganti akun: logout, lalu login sebagai Total Control client Batas Waktu (Pre-setup #15)
26. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action
27. Klik icon Download, pilih `Download as CSV`, lalu buka berkas dengan parser CSV
28. Verifikasi berkas berenkode UTF-8 dengan BOM pada byte awal
29. Verifikasi berkas memakai pemisah koma
30. Verifikasi sel Name baris BD-U5 tertulis `"Gedung ""Utama"", Lantai 1"` (dibungkus tanda kutip ganda dan tanda kutip digandakan)

## Notes

- Mode: FE+BE, kelas f (binary buffer): spec ini khusus isi sel, format berkas, urutan baris dan kolom; nama berkas dan jumlah baris ada di spec 046 dan 047.
- Satu unduhan CSV (langkah 2) dipakai bersama untuk TC-FA-FAAL-178 sampai 181 karena data (#12), format, dan General Settings staf identik; tiap TC punya `Verifikasi` sendiri atas berkas yang sama. Baris dikenali dari nilai Date dan Name seed.
- Pengelompokan `Verifikasi` (S-01): nilai beberapa kolom dari satu baris ditulis satu `Verifikasi` dengan daftar utuh (langkah 5, 7, 8); nilai dari baris berbeda dipisah.
- Urutan TC dalam spec berbeda dari nomor TC sumber (S-10): TC-FA-FAAL-185 berada di akhir karena memakai client Batas Waktu dan butuh ganti akun eksplisit (langkah 25).
- Langkah penghubung (S-03, S-09): langkah 1 (pindah tab), langkah 14 (menerapkan Filter Date Jendela Seed Tab User Action sesuai precondition d TC-FA-FAAL-187), langkah 18 (mengembalikan Sort Date ke netral), langkah 24 (memulihkan urutan kolom), langkah 26 (membuka layar di client Batas Waktu karena hook `beforeEach` membuka layar di client default).
- Temuan untuk QA:
  - TC-FA-FAAL-187 memberi precondition Filter Date Jendela Seed Tab User Action (18/06/26 sampai 18/06/26) agar baris data pertama default (UA-01) dan Oldest First (UA-15) tidak bergantung pada baris log lain; spec menerapkannya di langkah 14 dan mengikuti TC.
  - TC-FA-FAAL-185 tidak menyebut akun Total Control client Batas Waktu; akun itu disediakan tim FE tanpa karangan email; password memakai `Spectra.env.FA_TCBATAS_PASSWORD`.
  - TC-FA-FAAL-185 dan 186 tidak menyebut cara membaca byte awal dan daftar sheet; kemampuan parser tertulis di Prerequisites sebagai disediakan tim FE.
