---
id: TC-GS-TAG-E2E-065-sinkronisasi-brand-device-name-dan-sku-katalog
title: "Sinkronisasi Katalog dan Brand: Rename/Hapus Brand, Rename Device Name, dan Perubahan Model/Type SKU Tidak Mengubah Snapshot Tag"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-313
  - TC-GS-TAG-314
  - TC-GS-TAG-356
coverage:
  web: automated
---

# Sinkronisasi Katalog dan Brand: Rename/Hapus Brand, Rename Device Name, dan Perubahan Model/Type SKU Tidak Mengubah Snapshot Tag

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah Brand dan katalog (state global) dan memulihkannya di hook `after`; aksi hapus Brand ada di blok pertama pada Brand milik spec.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Rename dan hapus Brand dijalankan akun ini di Global Settings > Brand.
- Pemicu (P-2, sesi API, tidak diasersi): Principal approver (Mira Anggraini) `principalApprover_automated@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, mengubah Device Name dan Model/Type SKU katalog Admin Console (TC menyebut "Principal mengubah"; rencana menyebut akun Admin Console katalog; kesesuaian perlu dikonfirmasi tim FE saat tahap script, Q-2, kategori B). Mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30). Baris yang dipakai: DD-01 `E2801160600002054D8A0001` (Brand `Zebra`), DD-09 `356938035643501` (GPS Official; Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`, diaktivasi lewat Jalur A), satu tag Self-Purchased GPS Jalur B yang menyimpan ID Device Name `Teltonika FMB920` dari katalog (data khusus TC-GS-TAG-314 lewat fixture BE; identifier tidak ditetapkan TC dan disediakan tim FE/BE), sesi Activate di Event Log yang memuat DD-09 (disediakan tim FE/BE). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec.
- Data Brand (S-12, pengecualian nama literal): master Brand `Zebra` di Global Settings > Brand milik spec ini, di-seed idempotent oleh hook `before` (dilewati bila sudah ada), nama literal karena tag Seed Registri A bermerek `Zebra`; hook `after` menghapus sisa `Zebra` atau `Zebra Technologies` yang dibuat spec ini dan tidak menyentuh Brand lain.
- Kemampuan teknis (disediakan tim FE/BE): sesi API Principal untuk mengubah Device Name dan Model/Type SKU katalog Client A (dan memulihkannya); seeding tag Self-Purchased Jalur B yang menyimpan ID Device Name; seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan Device Name katalog ke `Teltonika FMB920` dan Model/Type SKU `SKU-GPS-01` ke `FMB920`, bersihkan Brand sisa, kembalikan Seed Registri A lewat fixture BE.
- Suite serial (`parallel: false`). State global yang diubah: Brand, katalog (Device Name, SKU) Client A; dipulihkan hook `after`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-313: Rename dan hapus Brand tidak mengubah Brand pada tag

1. Buka Global Settings > Brand
2. Ubah nama Brand `Zebra` menjadi `Zebra Technologies` lewat aksi Edit lalu `[Save]`
3. Hapus Brand `Zebra Technologies` lewat aksi Delete lalu konfirmasi
4. Verifikasi sedikitnya satu Brand lain tampil di daftar Brand
5. Verifikasi Brand `Zebra Technologies` tidak ada lagi di daftar Brand (penghapusan tidak diblok oleh keberadaan tag)
6. Buka Global Settings > TAG Tab All
7. Verifikasi kolom Brand baris DD-01 tetap `Zebra`
8. Buka Filter Panel
9. Verifikasi opsi filter Brand tetap memuat `Zebra`
10. Tutup Filter Panel

### TC-GS-TAG-314: Rename Device Name katalog, registri terkini, Detail Activate snapshot

11. Ubah Device Name katalog `Teltonika FMB920` menjadi `Teltonika FMB920 v2` lewat sesi API Principal hingga tersimpan
12. Muat ulang halaman Tab All
13. Ketik Search `356938035643501`, tekan Enter
14. Verifikasi sel Device Name DD-09 (Jalur A) `Teltonika FMB920 v2`
15. Ganti isi kotak search dengan identifier tag Self-Purchased Jalur B, tekan Enter
16. Verifikasi sel Device Name tag Self-Purchased Jalur B `Teltonika FMB920 v2`
17. Klik `(←)` pada kotak Search untuk mengosongkan pencarian
18. Buka Event Log > Tab Activate TAG
19. Klik `Detail` pada sesi Activate yang memuat DD-09
20. Verifikasi Detail Activate menampilkan Device Name `Teltonika FMB920` (snapshot)
21. Tutup popup Detail dan modal Event Log

### TC-GS-TAG-356: Perubahan Model/Type SKU katalog tidak mengubah tag

22. Ubah Model/Type SKU `SKU-GPS-01` di katalog menjadi `FMB920-R2` lewat sesi API Principal hingga tersimpan
23. Muat ulang halaman Tab All
24. Ketik Search `356938035643501`, tekan Enter
25. Verifikasi SKU baris DD-09 tetap `SKU-GPS-01`
26. Verifikasi Brand baris DD-09 tetap `Teltonika`
27. Verifikasi Model/Type baris DD-09 tetap `FMB920`
28. Verifikasi nilai `FMB920-R2` tidak tampil di registri

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian P-2: langkah 11 dan 22 hanyalah pemicu perubahan katalog lewat sesi API; objek asersi adalah sel registri dan Detail Activate. Perubahan Brand (langkah 2 dan 3) dijalankan langsung oleh Total Control Client A karena menjadi bagian aksi TC-GS-TAG-313.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 6 (navigasi antar modul), 8 dan 10 (membuka dan menutup Filter Panel untuk membaca opsi Brand), 12 dan 23 (memuat ulang halaman agar katalog terkini terbaca), 13, 15, 17, dan 24 (Search untuk menemukan baris target), 18 dan 21 (membuka dan menutup Event Log).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 (data pembanding sebagai anchor absence, bagian 8b butir 2).
- Temuan untuk QA:
  - Q-9: langkah dan selektor Admin Console katalog dan Global Settings > Brand (Edit, Delete, teks toast) tidak didefinisikan di TC; langkah 2 dan 3 mengikuti pola Edit `[Save]` dan Delete dengan konfirmasi dan teks toast tidak diasersi.
  - TC-GS-TAG-313 Expected b "tag tidak dihitung sebagai referensi" tidak menyebut tanda keberhasilan penghapusan (toast atau pesan); spec mengasersi Brand hilang dari daftar. Master Brand `Zebra` disebut ada di Global Settings > Brand tanpa menyebut Pre-setup Brand; spec men-seed Brand milik spec (S-12).
  - TC-GS-TAG-314 tidak menyebut identifier tag Self-Purchased Jalur B maupun sesi Event Log yang memuat DD-09; keduanya disediakan tim FE/BE.
  - TC-GS-TAG-314 dan 356 menyebut precondition "Principal mengubah ..." sebagai bagian precondition; spec menuliskan pengubahan itu sebagai langkah pemicu (langkah 11 dan 22) agar urutan state jelas.
  - Q-2: Pre-setup TC memakai `principalApprover_automated`, sedangkan `.env.example` mendaftarkan `totalControlPrincipal_automated_qaTeam1` (GS_PRINCIPAL_TC); kesamaan perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
  - Post Condition TC-GS-TAG-313, 314, dan 356 tidak ada.
