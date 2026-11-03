---
id: TC-AC-DS-E2E-108-state-list-refresh-reset-menu-dan-hapus-halaman-terakhir
title: "State List: Refresh F5, Klik Ulang Menu Settings, Isolasi Sub-tab, dan Hapus Semua Baris Halaman Terakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-366
  - TC-AC-DS-367
  - TC-AC-DS-368
  - TC-AC-DS-369
coverage:
  web: automated
---

# State List: Refresh F5, Klik Ulang Menu Settings, Isolasi Sub-tab, dan Hapus Semua Baris Halaman Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`, Brand `Arcturus`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Pohon Category, Device Name, dan Brand (#25, #26, #27) dibaca untuk seeding data khusus TC. File foto (#37).
- Data khusus TC (Pre-setup #44, milik TC-AC-DS-366; nama literal mengikuti TC), di-seed idempoten lewat API di hook `before` (jumlah total N dari seeding, bukan dari tabel): 29 SKU `PGD-001` sampai `PGD-029` (Device Name `Seed Tag`, Category `Asset TAG`, Brand `Arcturus`, Model/Type `PGD`, stok 0, 1 foto). Search `PGD` menghasilkan 29 baris; pada 10 data per halaman halaman 1 dan 2 berisi 10 baris dan halaman 3 (halaman terakhir) berisi 9 baris (`PGD-021` sampai `PGD-029`). Hook `after` menghapus sisa SKU `PGD-*` lewat API tanpa mengasumsikan seeding atau langkah 31 berhasil penuh. Pemulihan jumlah SKU (129) dan Changelog (35 entri) dilakukan baseline data uji yang disediakan tim FE/BE.
- Nilai data diacu lewat `Fixture.settingsDeviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-367: Refresh F5 mempertahankan state

1. Ketik Search `SEED`, tekan Enter
2. Klik ikon Filter
3. Pada field Brand pilih `Arcturus`
4. Klik `[Apply]`
5. Klik header kolom SKU dua kali sampai Descending aktif
6. Ubah jumlah data per halaman menjadi 25, lalu pindah ke halaman 2
7. Catat baris pertama halaman 2
8. Muat ulang halaman dengan F5
9. Verifikasi Search `SEED` dipertahankan setelah F5
10. Verifikasi Filter Brand `Arcturus` dipertahankan setelah F5
11. Verifikasi Sort SKU Descending dipertahankan setelah F5
12. Verifikasi 25 per halaman dipertahankan setelah F5
13. Verifikasi halaman 2 dipertahankan setelah F5
14. Verifikasi baris pertama halaman 2 sama dengan yang dicatat di langkah 7

### Pemulihan state antar TC

15. Ubah jumlah data per halaman menjadi 10

### TC-AC-DS-368: Klik ulang menu Settings

16. Klik item sidebar `Settings`, lalu pilih Device > Device SKU
17. Verifikasi Search kosong
18. Verifikasi Sort default SKU A-Z
19. Verifikasi Filter kosong
20. Verifikasi tabel berada di halaman 1

### TC-AC-DS-369: Isolasi sub-tab Device Name

21. Ketik Search `SEED`, tekan Enter
22. Klik nomor halaman 2
23. Klik sub-tab `Device Name`
24. Verifikasi state sub-tab Device Name tidak berubah oleh aktivitas di Device SKU: Search kosong dan halaman 1
25. Klik sub-tab `Device SKU`
26. Verifikasi Search `SEED` dipulihkan pada sub-tab Device SKU
27. Verifikasi halaman 2 dipulihkan pada sub-tab Device SKU

### TC-AC-DS-366: Hapus semua baris halaman terakhir

28. Ganti isi kotak search dengan `PGD`, tekan Enter
29. Klik nomor halaman 3 (halaman terakhir, 9 baris: `PGD-021` sampai `PGD-029`)
30. Klik checkbox header
31. Pilih aksi Delete dari Bulk Action, lalu klik `[Delete]`
32. Verifikasi muncul toast sukses: "Success, device SKU has been deleted."
33. Verifikasi tabel berpindah ke halaman 2 (halaman terakhir yang masih ada)
34. Verifikasi tabel tidak menampilkan halaman kosong: 10 baris `PGD-...` tampil
35. Klik `(←)` pada kotak Search

## Notes

- Urutan blok: TC-AC-DS-366 (aksi hapus) dikerjakan terakhir; sumber memuatnya lebih dulu.
- Langkah 1 sampai 7 pada TC-AC-DS-367 meninggalkan Search, Filter, Sort, dan ukuran halaman aktif; klik sidebar di langkah 16 mereset semuanya (superset state TC-AC-DS-368, yang hanya memakai Search `SEED`). Langkah 21 memasang Search `SEED` kembali.
- Langkah penghubung (S-03, S-09, S-14): langkah 15 mengembalikan ukuran halaman 25 (diubah langkah 6) ke 10 sebelum blok berikutnya, karena TC-AC-DS-366 memakai 10 data per halaman (29 baris menjadi halaman 3 berisi 9 baris); tanpa asersi.
- Langkah penghubung (S-03, R-16): langkah 28 mencari baris data khusus TC karena tabel memuat lebih dari satu halaman; langkah 35 menutup Search; tanpa asersi tambahan.
- Temuan untuk QA:
  - TC-AC-DS-366 memakai data khusus Pre-setup #44 (`PGD-001` sampai `PGD-029`, Search `PGD`, halaman terakhir halaman 3 berisi 9 baris, setelah hapus ke halaman 2); spec mengikuti TC, tidak memakai `SEED-111` sampai `SEED-119` (Pre-setup #30) sehingga Pre-setup bersama tidak berubah (S-06).
  - TC-AC-DS-366 tidak menyebut apakah checkbox header memilih baris halaman aktif atau seluruh hasil; spec mengikuti redaksi TC.
  - TC-AC-DS-369 Expected b ("state sub-tab Device Name tidak berubah") tidak menyebut keadaan awalnya; spec mengasersi keadaan default (Search kosong, halaman 1).
  - S-12: nama literal Pre-setup #29 dan #30 dipakai sesuai pengecualian S-12 A-11 (`suite.md`). Pre-setup #44 (`PGD-001` sampai `PGD-029`, nama literal tanpa suffix `{runId}`) tidak tercantum di A-11; spec mengikuti TC (Search `PGD`) dan butuh keputusan pengecualian.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.settingsDeviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
