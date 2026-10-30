---
id: TC-GS-TAG-E2E-026-unggah-berkas-csv-xlsx-gps
title: "Unggah Berkas GPS: CSV Kolom IMEI, XLSX Sheet Pertama, Tanpa Kolom IMEI T-12, dan Berkas Tidak Valid T-33"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-73
  - TC-GS-TAG-74
  - TC-GS-TAG-75
  - TC-GS-TAG-76
coverage:
  web: automated
---

# Unggah Berkas GPS: CSV Kolom IMEI, XLSX Sheet Pertama, Tanpa Kolom IMEI T-12, dan Berkas Tidak Valid T-33

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Stok resmi Admin Console Client A (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`) di-seed idempotent oleh fixture BE di hook `before`: GPS `356938035643001` (DD-S1) dan GPS `356938035643003` (DD-S3) Available. Akun Admin Console untuk seeding stok disediakan tim FE (S-13).
- Berkas uji (disediakan tim FE; nama berkas ditentukan di tahap script, isi sesuai TC):

  | Berkas | Isi | Dipakai TC |
  |---|---|---|
  | CSV kolom IMEI | header ` imei ` (huruf kecil, berspasi) dan `Notes`; baris data `356938035643001`, `356938035643003` | TC-73 |
  | XLSX dua sheet | Sheet1 header `IMEI` dan `356938035643001`; Sheet2 `356938035643003` | TC-74 |
  | CSV tanpa kolom IMEI | header `Serial` dan `Notes` | TC-75 |
  | Berkas `.pdf` | berkas PDF apa pun | TC-76 |
  | Berkas melebihi batas ukuran | ukuran melebihi batas pada `global-settings/import/PRD/import.md` §6.1 (nilai tidak di-hardcode TC) | TC-76 |
  | CSV header saja | header `IMEI` tanpa baris data | TC-76 |

- Opsi mandiri (BYO) aktif untuk Client A; Template Self-Purchased kosong pada awal tiap sesi Activate.
- Kemampuan teknis: unggah berkas ke dropzone CSV/XLSX pada halaman Activate GPS (label dan selektor dropzone menunggu desain, NC-11, disediakan tim FE); entri manual GPS (input teks dan tombol `Add`).
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Sesi 1

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-76: Berkas tidak valid ditolak T-33

2. Unggah berkas `.pdf`
3. Verifikasi toast error persisten `Error, the uploaded file is invalid. Please check the file format, size, and content.` untuk berkas `.pdf`
4. Unggah berkas yang melebihi batas ukuran
5. Verifikasi toast error persisten yang sama untuk berkas melebihi batas
6. Unggah CSV berisi header `IMEI` saja tanpa baris data
7. Verifikasi toast error persisten yang sama untuk CSV tanpa baris data
8. Verifikasi tidak ada baris masuk staging untuk berkas `.pdf`, berkas besar, maupun CSV tanpa data (all-or-nothing)

### TC-GS-TAG-75: Berkas tanpa kolom IMEI ditolak T-12

9. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
10. Unggah CSV dengan header `Serial` dan `Notes`
11. Verifikasi toast error persisten `Error, the uploaded file doesn't contain an IMEI column.`
12. Verifikasi tidak ada baris baru di staging
13. Verifikasi baris `356938035643001` tetap di staging
14. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 2

15. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-73: Unggah CSV dengan kolom IMEI

16. Unggah CSV dengan header ` imei ` dan `Notes`, baris data `356938035643001` dan `356938035643003`
17. Verifikasi dua baris `356938035643001` dan `356938035643003` masuk staging sebagai `Official`
18. Verifikasi kolom `Notes` diabaikan (tidak ada data `Notes` di tabel staging)
19. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 3

20. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-74: Unggah XLSX, hanya sheet pertama dibaca

21. Unggah XLSX dengan Sheet1 berisi header `IMEI` dan `356938035643001`, Sheet2 berisi `356938035643003`
22. Verifikasi hanya `356938035643001` masuk staging
23. Verifikasi `356938035643003` dari Sheet2 tidak dibaca
24. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (unggah berkas); berkas uji disediakan tim FE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: sesi 1 memuat kasus ditolak (TC-76, TC-75) lebih dulu; TC-76 mendahului TC-75 karena staging harus kosong untuk memastikan "tidak ada baris masuk". Sesi 2 dan 3 dipisah karena TC-73 dan TC-74 memakai identifier yang sama (`356938035643001`, `356938035643003`).
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Tambahkan ... 356938035643001` pada TC-75 menjalankan TC langkah 4; `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-76 Langkah 5 merujuk batas ukuran berkas pada `global-settings/import/PRD/import.md` §6.1 tanpa angka; ukuran berkas uji ditentukan tim FE.
  - TC-75 dan TC-76: toast error bersifat persisten tetapi TC tidak menyatakan cara menutupnya; tiga unggahan beruntun pada TC-76 dapat menumpuk toast yang sama, dan spec memverifikasi muncul toast tiap unggahan tanpa langkah menutup (menunggu jawaban QA).
  - TC-73 Expected ("kolom `Notes` diabaikan") tidak punya ukuran teramati selain tidak adanya kolom/data `Notes` di staging.
