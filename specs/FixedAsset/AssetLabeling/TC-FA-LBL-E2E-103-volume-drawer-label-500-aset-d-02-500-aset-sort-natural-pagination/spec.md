---
id: TC-FA-LBL-E2E-103-volume-drawer-label-500-aset-d-02-500-aset-sort-natural-pagination
title: "Volume: Drawer Label 500 Aset (D-02 500 Aset, Sort Natural, Pagination)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-167
  - TC-FA-LBL-355
  - TC-FA-LBL-372
coverage:
  web: automated
---

# Volume: Drawer Label 500 Aset (D-02 500 Aset, Sort Natural, Pagination)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Extra (Pre-setup #56: salinan label Pre-setup #12 plus seed tambahan), `Fixture.assetLabeling.akun.totalControlExtra`. Nama company, email akun (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), dan nama env password belum ada, disediakan tim FE; tidak diisi di spec. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Hook `after` suite mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #18 (volume, hanya dibaca; kelas e; di Company Extra, Pre-setup #56): label `Bulk Heavy` terpasang pada 500 aset `Laptop Dell - 1` sampai `Laptop Dell - 500` (disiapkan lewat API oleh tim FE/BE). N total = 500 diturunkan dari seeding, bukan dibaca dari tabel yang hanya menampilkan satu halaman (bagian 8b butir 10). Fixture label: `Fixture.assetLabeling.labelBulkHeavy` (`Bulk Heavy`).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.
- Kemampuan teknis: kemampuan baca state BE (jumlah aset berlabel `Bulk Heavy`) dan baca jumlah entri log Changelog Labels, System Log, dan Activity Log sebelum dan sesudah aksi, disediakan tim FE/BE (bagian 8b butir 10); tanpa endpoint karangan.

## Test Steps

### TC-FA-LBL-167: Delete label yang dipakai 500 aset menyebut 500 aset di D-02

1. Catat baseline jumlah entri log milik Company Extra pada tiga permukaan: Modal Changelog: Labels, System Log, dan Activity Log
2. Ketik Search `Bulk Heavy` di kotak Search Labels List, tekan Enter
3. Klik `⋯` pada baris `Bulk Heavy`, lalu klik `Delete`
4. Verifikasi dialog `Cannot Delete Label` dengan baris `This label is assigned to 500 assets.` tampil
5. Verifikasi jumlah entri Modal Changelog: Labels sama dengan baseline (tidak ada log)
6. Verifikasi jumlah entri System Log sama dengan baseline (tidak ada log)
7. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada log)
8. Klik `[OK]` pada dialog `Cannot Delete Label`
9. Verifikasi tidak ada mutasi pada Labels List: baris `Bulk Heavy` tetap ada dengan Total Asset `500`
10. Verifikasi tidak ada mutasi pada penempelan: seluruh 500 aset `Laptop Dell - 1` sampai `Laptop Dell - 500` tetap berlabel `Bulk Heavy` (dibaca lewat fixture BE)

### TC-FA-LBL-355: Sort Drawer kolom Name: alfabetis nama aset lalu Increment numerik natural

11. Klik chip `Bulk Heavy` di kolom Label
12. Verifikasi default sort: `Laptop Dell - 1`, `Laptop Dell - 2`, `Laptop Dell - 3`, ... `Laptop Dell - 9`, `Laptop Dell - 10` (bukan 1, 10, 100, 11)
13. Klik header `Name` satu kali
14. Verifikasi klik 1 (Ascending) sama dengan default
15. Klik header `Name` sekali lagi (klik kedua)
16. Verifikasi klik 2 (Descending) dimulai `Laptop Dell - 500`, `Laptop Dell - 499`
17. Klik header `Name` sekali lagi (klik ketiga)
18. Verifikasi klik 3 kembali ke default

### TC-FA-LBL-372: Pagination Drawer: default 10, pilihan page size, dan navigasi

19. Verifikasi Drawer menampilkan default 10 baris
20. Verifikasi info total `500`
21. Buka pilihan page size
22. Verifikasi pilihan page size `10`, `25`, `50`, dan `100`
23. Ganti page size menjadi 25
24. Ganti page size menjadi 50
25. Ganti page size menjadi 100
26. Ganti page size kembali menjadi 10
27. Pindah ke halaman 2
28. Verifikasi halaman 2 aktif menampilkan `Laptop Dell - 11` sampai `Laptop Dell - 20`
29. Pindah ke halaman 50
30. Verifikasi halaman 50 aktif menampilkan `Laptop Dell - 491` sampai `Laptop Dell - 500`
31. Tutup Drawer dengan `[✕]`, lalu klik `(←)` pada kotak Search Labels List

## Notes

- Mode: FE+BE (backend nyata). Kelas harness e (volume data khusus: 500 aset). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 3c (Delete Label) dan section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- P-1: `Verifikasi` tidak ada log pada TC-FA-LBL-167 (langkah 5 sampai 7) ditulis di spec ini karena konteksnya bergantung pada state berat Pre-setup #18 (label dengan 500 aset, seeding berat yang sama dengan aksi TC); asersi absence berbaseline (S-12). Anchor positif: dialog `Cannot Delete Label` tampil dan baseline tercatat (bagian 8b butir 2).
- TC-FA-LBL-355 dan TC-FA-LBL-372 memakai satu pembukaan Drawer `Bulk Heavy` (tanpa perubahan state data).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): baseline log (S-12); Search `Bulk Heavy` pada Labels List untuk menemukan baris target (label tambahan Pre-setup #18 mungkin tidak berada di halaman pertama); `[OK]` untuk menutup dialog; mengembalikan page size ke 10 sebelum pindah halaman; membersihkan Search Labels List di langkah terakhir.
- Asersi turunan (S-03): `Verifikasi` isi halaman 2 dan halaman 50 pada TC-FA-LBL-372 diturunkan dari Expected 'navigasi halaman berfungsi', sort default natural (TC-FA-LBL-355), dan 500 aset berpage size 10; `Verifikasi` isi baris itu tidak ada di Expected TC.
- Pembagian TC lintas spec: TC-FA-LBL-168 (OK pada D-02 tanpa mutasi dan tanpa log) ada di spec Absence Log; TC-FA-LBL-356 dan TC-FA-LBL-357 ada di spec 097; TC-FA-LBL-358 sampai TC-FA-LBL-361 ada di spec 098.
- Temuan untuk QA:
  - TC-FA-LBL-167 menyebut 'tidak ada log' tanpa merinci permukaan log; spec mengasersi tiga permukaan (Modal Changelog: Labels, System Log, Activity Log) dengan baseline.
  - TC-FA-LBL-167 tidak menyebut cara menutup dialog `Cannot Delete Label`; tombol `[OK]` diambil dari judul TC-FA-LBL-168.
  - TC-FA-LBL-372 mengganti page size menjadi 25, 50, 100 lalu pindah ke halaman 50; pada page size 100 hanya ada 5 halaman, sehingga spec mengembalikan page size ke 10 sebelum menavigasi (halaman 50 hanya ada pada page size 10). TC tidak menyebut hasil per page size 25, 50, dan 100, sehingga jumlah baris per page size tidak diasersi.
  - Company Extra (Pre-setup #56) memuat salinan label Pre-setup #12 plus seed tambahan; baris `Bulk Heavy` dicari lewat Search dan posisi halamannya ditentukan tim FE.
