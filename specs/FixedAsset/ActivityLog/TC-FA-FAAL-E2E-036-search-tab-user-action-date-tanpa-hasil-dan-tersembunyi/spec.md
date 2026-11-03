---
id: TC-FA-FAAL-E2E-036-search-tab-user-action-date-tanpa-hasil-dan-tersembunyi
title: "Search Tab User Action: Kolom Date Tidak Dicari, Tanpa Hasil, dan Kolom Field Tersembunyi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-123
  - TC-FA-FAAL-124
  - TC-FA-FAAL-125
coverage:
  web: automated
---

# Search Tab User Action: Kolom Date Tidak Dicari, Tanpa Hasil, dan Kolom Field Tersembunyi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session); langkah 1 membuka Tab User Action. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #12 (Tab User Action UA-01 sampai UA-15, tanggal 18/06/26 Asia/Jakarta, format tanggal `dd/MM/yy`), hanya dibaca dan tidak diubah. Baris yang dipakai pada langkah 16: UA-02, UA-11, UA-13, UA-14, dan UA-15 (kolom Field `Group Name`). Identitas baris dirujuk lewat `Fixture.activity-log.<kunci>` (fixture `fixtures/activity-log.json` disediakan tim FE; nama kunci ditetapkan tim FE).
- Nilai Data Uji TC: Search `18/06/26`, `Jun`, `zzzz`, dan `Group Name` (dirujuk lewat fixture yang sama).
- Jendela Seed Tab User Action: Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15), diterapkan di langkah 2 (precondition TC-FA-FAAL-125) sehingga baris yang diasersi hanya baris seed #12; total entri tidak diasersi.
- State yang diubah spec: Filter Date, Search Tab User Action, dan visibilitas kolom Field. Langkah 14 menampilkan kembali kolom Field; hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`. Search dan Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab User Action
2. Klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-123: Search tidak mencocokkan kolom Date Tab User Action

3. Ketik Search `18/06/26`, tekan Enter
4. Verifikasi tabel menampilkan state `No results found`
5. Ganti isi kotak search dengan `Jun`, tekan Enter
6. Verifikasi tabel menampilkan state `No results found`

### TC-FA-FAAL-124: Search tanpa hasil di Tab User Action menampilkan state kosong terfilter

7. Ganti isi kotak search dengan `zzzz`, tekan Enter
8. Verifikasi tampil Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
9. Verifikasi tidak ada baris tabel dan tidak ada pesan error

### TC-FA-FAAL-125: Search tidak mencari kolom Field yang disembunyikan

10. Klik header Actions (⋯), hilangkan centang kolom Field di overlay Column Visibility
11. Ganti isi kotak search dengan `Group Name`, tekan Enter
12. Verifikasi tabel menampilkan state `No results found` saat kolom Field disembunyikan
13. Kosongkan isi kotak search, tekan Enter
14. Klik header Actions (⋯), centang kembali kolom Field di overlay Column Visibility
15. Ketik Search `Group Name`, tekan Enter
16. Verifikasi tabel menampilkan UA-02, UA-11, UA-13, UA-14, dan UA-15 setelah kolom Field ditampilkan

## Notes

- Langkah penghubung (S-03): langkah 1 (pindah ke Tab User Action karena layar awal suite adalah Tab Session); langkah 13 (mengosongkan Search sebelum menampilkan kembali kolom Field, sesuai TC-FA-FAAL-125 langkah 3). Langkah 14 menampilkan kembali kolom Field sekaligus memulihkan state (R-08).
- Langkah 2 (S-03): menerapkan Filter Date Jendela Seed Tab User Action sesuai precondition d TC-FA-FAAL-125.
- Langkah 4 dan 6: TC-FA-FAAL-123 menulis satu Expected untuk kedua keyword ("Kedua keyword menghasilkan state `No results found`"); spec memberi satu `Verifikasi` per keyword (S-01). Kalimat "kolom Date tidak Searchable" pada Expected TC adalah alasan, bukan klausa teramati terpisah.
- Langkah 4, 6, dan 12 memuat `No results found` sebagai anchor positif hasil Search; langkah 9 (daftar elemen yang sama-sama tidak ada) disebut utuh dalam satu `Verifikasi` (S-01).
- Langkah 16 menyebut daftar baris seed sekaligus sebagai pembanding positif asersi hasil Search.
- Temuan untuk QA:
  - TC-FA-FAAL-125 memberi precondition Filter Date Jendela Seed Tab User Action (18/06/26 sampai 18/06/26) agar hasil Search tidak bergantung pada baris log lain; spec menerapkannya di langkah 2 dan mengikuti TC. TC-FA-FAAL-123 dan 124 tidak memuat Filter Date dan asersinya `No results found`.
  - TC-FA-FAAL-123 memakai keyword `Jun` yang berpotensi cocok dengan nilai kolom lain selain Date (misalnya Name atau Note yang mengandung `Jun`); data seed #12 tidak memuat nilai itu sehingga Expected `No results found` hanya berlaku pada seed tersebut.
  - TC-FA-FAAL-125 langkah 3 menulis "Kosongkan input" tanpa menyebut Enter; spec menulis "kosongkan isi kotak search, tekan Enter" agar tabel kembali tanpa Search.
