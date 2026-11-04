---
id: TC-FA-LBL-E2E-064-sinkron-delete-dan-bulk-delete-label-ke-konsumen-lintas-modul
title: "Sync Matrix: Delete dan Bulk Delete Label hilang dari asset/, reports/, dan settings-asset-name/"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:sync-matrix/delete-label-single
  - FALB:sync-matrix/bulk-delete-labels
coverage:
  web: automated
---

# Sync Matrix: Delete dan Bulk Delete Label hilang dari asset/, reports/, dan settings-asset-name/

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Tidak ada ganti akun.
- Data uji `DU-70` (Label seed untuk uji konsumen lintas modul), bersuffix `{runId}-064`, dibuat lewat sesi API di hook `before` dan dihapus di hook `after` (relasi label, aset, Asset Name, lalu label): label bersih `Sync-{runId}-064-s` (target Delete single, disebut label S), dua label bersih `Sync-{runId}-064-b1` dan `Sync-{runId}-064-b2` (target Bulk Delete, disebut B1 dan B2), label pembanding `Sync-{runId}-064-k` yang menempel pada aset Active seed dan tidak dihapus (label K), serta satu Asset Name seed. Satu Search `DU-70` menampilkan keempat label. Aksi hapus berada di akhir bagian masing-masing.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, aset, dan Asset Name, disediakan tim FE/BE. Halaman Asset Detail dimiliki modul `asset/` (`asset/PRD/asset.md` §4.1d); Modal Edit Asset Name dengan dropdown Default Label dimiliki modul `settings-asset-name/` (§4.1).
- State global: spec menghapus label S, B1, dan B2 lewat UI; hook `after` membersihkan sisa seed. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:sync-matrix/delete-label-single: Delete Label (Single): opsi label hilang dari dropdown penugasan asset/ dan opsi Default Label settings-asset-name/

1. Ketik Search `DU-70`, tekan Enter
2. Verifikasi keempat label milik `DU-70` (S, B1, B2, dan K) tampil pada Labels List
3. Klik `[⋯]` pada baris label S, pilih `Delete`
4. Verifikasi dialog `Delete Label` tampil dengan nama label S
5. Klik `[Delete]`
6. Verifikasi toast `Success, label has been deleted.` tampil
7. Verifikasi baris label S tidak tampil pada Labels List
8. Buka Asset Detail aset seed `DU-70` dari Asset List modul `asset/`
9. Verifikasi chip label K tampil pada seksi Labels
10. Klik `[+ Add Label]` pada seksi Labels
11. Verifikasi label B1 tampil sebagai opsi pada dropdown penugasan label sedangkan label S tidak tampil
12. Tutup dropdown penugasan label
13. Buka Modal Edit Asset Name seed `DU-70` dari tab Asset Name pada Settings > Asset Master
14. Klik dropdown Default Label pada Modal Edit Asset Name
15. Verifikasi label K dan B1 tampil sebagai opsi pada dropdown Default Label sedangkan label S tidak tampil
16. Klik `[✕]` pada header Modal Edit Asset Name

### FALB:sync-matrix/bulk-delete-labels: Bulk Delete Labels: opsi label hilang dari dropdown penugasan asset/ dan opsi Default Label settings-asset-name/

17. Buka tab Labels pada Settings > Asset Master
18. Ketik Search `DU-70`, tekan Enter
19. Centang checkbox baris label B1 dan B2
20. Klik `Delete` pada Bulk Action Bar
21. Verifikasi dialog `Delete Labels` tampil dengan daftar label B1 dan B2 serta teks `Are you sure you want to delete them? This action cannot be undone.`
22. Klik `[Delete]`
23. Verifikasi toast `Success, label has been deleted.` tampil
24. Verifikasi baris label B1 dan B2 tidak tampil pada Labels List
25. Buka Asset Detail aset seed `DU-70` dari Asset List modul `asset/`
26. Verifikasi chip label K tampil pada seksi Labels
27. Klik `[+ Add Label]` pada seksi Labels
28. Verifikasi label B1 dan B2 tidak tampil sebagai opsi pada dropdown penugasan label
29. Tutup dropdown penugasan label
30. Buka Modal Edit Asset Name seed `DU-70` dari tab Asset Name pada Settings > Asset Master
31. Klik dropdown Default Label pada Modal Edit Asset Name
32. Verifikasi label K tampil sebagai opsi pada dropdown Default Label sedangkan label B1 dan B2 tidak tampil
33. Klik `[✕]` pada header Modal Edit Asset Name

## Notes

- Langkah penghubung (S-03): langkah 1 dan 18 menemukan baris label target di Labels List yang dapat memuat lebih dari satu halaman (R-16); langkah 8, 13, 17, 25, dan 30 berpindah halaman atau modul; langkah 12, 16, 29, dan 33 menutup dropdown dan modal tanpa perubahan.
- Anchor absence (bagian 8b butir 2): toast sukses Delete (langkah 6 dan 23) menjadi anchor untuk baris label hilang dari Labels List (langkah 7 dan 24); untuk dropdown, langkah 9 dan 26 (chip label K tampil pada seksi Labels) serta opsi pembanding B1 atau K pada surface dropdown yang sama (langkah 11, 15, dan 32) mendahului asersi label yang dihapus tidak tampil.
- Timing sync: Delete single dan Bulk Delete bersifat "Transaksi Atomik (Sync)" (PRD §9.7); asersi dilakukan setelah toast hasil server tanpa menunggu waktu tertentu.
- Temuan PRD: sync-matrix menyebut "filter `reports/`" sebagai surface terdampak untuk Delete dan Bulk Delete, tetapi PRD ini hanya menyebut path modul `reports/` tanpa nama halaman atau filter, dan modul `reports/` tidak memiliki PRD di repositori dokumentasi; klausa `reports/` tidak diasersi.
- Temuan PRD: baris Bulk Delete menyatakan "Memperbarui cache list katalog label; label yang dipakai tidak berubah" tanpa surface yang dapat diamati untuk label yang dipakai; label K (dipakai aset seed) hanya dipakai sebagai pembanding tampil (langkah 9, 15, 26, dan 32).
