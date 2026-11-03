---
id: TC-FA-TAG-E2E-271-derivasi-tanpa-objek-tugas-changelog-immutable-dan-tag-log-sebagai
title: "Derivasi Tanpa Objek Tugas, Changelog Tidak Dapat Diubah, dan Popup TAG Log sebagai Satu-satunya Pintu Riwayat Status Tag"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1072
  - TC-FA-TAG-1073
  - TC-FA-TAG-1074
  - TC-FA-TAG-1075
  - TC-FA-TAG-1076
  - TC-FA-TAG-1077
coverage:
  web: automated
---

# Derivasi Tanpa Objek Tugas, Changelog Tidak Dapat Diubah, dan Popup TAG Log sebagai Satu-satunya Pintu Riwayat Status Tag

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akun aktor: Manage asset & TAG (Read + Update) (Update: Plant A) [MU_PA] `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_MU_PA_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai pada blok TC-FA-TAG-1074 (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): grup Excavator 20 Ton / Plant A dan Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A (Non TAG); Tag RF-00900 (Available), RF-00901 (Damaged/Missing), RF-00902 (Retired) di registri Global; RF-00101 Paired pada AST-0011 dan terakhir dipindai pada sesi audit aset AST-0020; Changelog memuat entri Replace (seed) serta entri Report TAG untuk `Excavator 20 Ton - 201` (Plant A) dan `Excavator 20 Ton - 20` (Plant B).
- Baseline jumlah baris Approvals dan Change Document dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before`, sebelum aksi pemicu (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): TAG Type 'Excavator 20 Ton' kembali RFID dan data seed dipulihkan lewat fixture backend.
- State global: TAG Type Asset Name 'Excavator 20 Ton' diubah pada TC-FA-TAG-1072. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1072: perubahan TAG Type tidak membuat tugas atau dokumen

1. Pada Fixed Asset > Settings > Asset Name ubah TAG Type 'Excavator 20 Ton' dari RFID menjadi NFC lalu klik [Save]
2. Tunggu aksi selesai (Save Asset Name selesai dan halaman kembali ke daftar)
3. Buka menu Approvals
4. Verifikasi jumlah baris Approvals sama dengan baseline: tidak ada tugas atau approval baru untuk Replace TAG
5. Buka menu Change Document
6. Verifikasi jumlah baris Change Document sama dengan baseline: tidak ada dokumen baru untuk Replace TAG
7. Kembalikan TAG Type 'Excavator 20 Ton' ke RFID lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-1073: entri Changelog tidak dapat diubah atau dihapus

8. Klik tombol `Changelog`
9. Verifikasi Modal Changelog memuat sedikitnya satu entri Replace (entri seed)
10. Verifikasi tidak ada kontrol Edit atau Delete pada setiap entri Changelog
11. Tutup Modal Changelog

### TC-FA-TAG-1075: Tag selain Paired tidak tampil di tab Paired

12. Ketik Search `RF-0090`, tekan Enter
13. Verifikasi Illustration `No results found`: Tag RF-00900 (Available), RF-00901 (Damaged/Missing), RF-00902 (Retired) tidak tampil di tab Paired
14. Verifikasi tab Paired hanya menampilkan Tag berstatus Paired, sedangkan Tag To be Returned hanya tampil di tab To Be Returned
15. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-TAG-1076: kepemilikan Tag mengikuti pairing aktif

16. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
17. Verifikasi `RF-00101` tampil pada baris AST-0011 (kolom TAG Code)
18. Verifikasi `RF-00101` tidak tampil pada baris AST-0020 (kolom TAG Code)

### TC-FA-TAG-1077: Popup TAG Log sebagai satu-satunya pintu riwayat status Tag

19. Klik `RF-00101` pada Popup Detail
20. Verifikasi Popup TAG Log (milik all-tags) terbuka
21. Tutup Popup TAG Log dan Popup Detail
22. Klik tombol `Changelog`
23. Verifikasi Modal Changelog tidak menampilkan riwayat status per Tag
24. Tutup Modal Changelog, lalu ganti akun: logout dari akun Total Control
25. Login dengan akun Manage asset & TAG (Read + Update) (Update: Plant A) [MU_PA] lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-1074: Changelog Report TAG sesuai scope group

26. Klik tombol `Changelog`
27. Verifikasi entri Report TAG untuk `Excavator 20 Ton - 201` (Plant A) tampil
28. Verifikasi entri Report TAG dengan Name persis `Excavator 20 Ton - 20` (Plant B, bukan `Excavator 20 Ton - 201`) tidak tampil

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 2, 7, 11, 15, 21, 24 dan 25 (menunggu aksi selesai, mengembalikan TAG Type, menutup popup dan modal, mereset Search, ganti akun).
- Urutan TC-FA-TAG-1074 diletakkan terakhir karena butuh akun MU_PA (ganti akun eksplisit, S-07); TC-FA-TAG-1077 melanjutkan Popup Detail yang dibuka pada TC-FA-TAG-1076.
- Temuan untuk QA:
  - TC-FA-TAG-1072 sampai 1077 Post Condition ('Tidak ada perubahan data bisnis') tidak punya langkah observasi; tidak diasersi.
  - TC-FA-TAG-1072 Expected ('Tidak ada tugas, dokumen, atau approval baru') tidak menyebut cara membuktikan tidak adanya; spec memakai jumlah baris Approvals dan Change Document terhadap baseline.
  - TC-FA-TAG-1075 Expected b ('hanya status Paired dan To Be Returned yang tampil di FAMS') adalah kesimpulan; langkah TC hanya mencari di tab Paired, tab To Be Returned tidak dicari. Spec mengasersinya sebagai satu `Verifikasi` tanpa langkah tambahan.
  - TC-FA-TAG-1077 Expected ('riwayat status per Tag tidak ditampilkan di Modal Changelog') tidak punya langkah membuka Changelog; spec menambah langkah penghubung menutup popup dan membuka Changelog (S-14).
  - TC-FA-TAG-1074 menyebut Name `Excavator 20 Ton - 20` dan `Excavator 20 Ton - 201`; yang pertama adalah awalan yang kedua, sehingga asersi absence memakai kecocokan nama persis (R-13).
