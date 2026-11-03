---
id: TC-FA-CAID-E2E-048-multi-konteks-dua-admin-status-sama-dan-sinkron-surface
title: "Multi-Konteks: Dua Admin Toggle ke Status Sama dan Sinkron Surface Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-328
  - TC-FA-CAID-329
coverage:
  web: automated
---

# Multi-Konteks: Dua Admin Toggle ke Status Sama dan Sinkron Surface Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: sesi 1 Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`; sesi 2 Total Control sesi kedua `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 8), password `Spectra.env.FA_TC2_PASSWORD`; sesi 3 Total Control (Pre-setup No 1) pada konteks browser ketiga dengan password `Spectra.env.FA_TC_PASSWORD`, dipakai hanya pada TC-FA-CAID-329. Ketiganya login di hook `before` spec ini pada konteks browser terpisah (Company Alpha dua sesi, Pre-setup No 23); sesi 1 membuka halaman lewat hook `beforeEach` suite, sesi 2 dan sesi 3 ditutup di hook `after`.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan aksi bersamaan pada dua sesi UI (disediakan tim FE; TC berlabel Manual Only karena dua sesi paralel); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12). Jendela amat propagasi antar sesi: 5 detik tanpa memuat ulang halaman, pilihan spec ini (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Master Switch dan Separator Company Alpha berubah, Asset ID aset berubah. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-328: Dua admin menggeser Master Switch ke status yang sama

1. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID di sesi 1 dan sesi 2, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log, dan Activity Log
2. Di sesi 1 dan sesi 2 geser Master Switch ke OFF lalu klik `[Disable]` hampir bersamaan
3. Verifikasi satu sesi menerima toast sukses `Success, Custom Asset ID configuration has been updated.`
4. Verifikasi sesi lainnya menerima toast netral `No changes to save.`
5. Muat ulang sesi 1 dan sesi 2
6. Buka Fixed Asset > Assets > All Assets di sesi 1
7. Verifikasi Asset ID A1, A2, A3 berupa `1`, `2`, `3`
8. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID di sesi 1, lalu buka Modal Changelog: Custom Asset ID
9. Verifikasi Changelog bertambah tepat satu entri dibanding baseline (Edit Status Old Value `Active`, New Value `Inactive`)
10. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
11. Verifikasi System Log bertambah tepat satu entri dibanding baseline (Edit Status Old Value `Active`, New Value `Inactive`)
12. Buka Fixed Asset > Activity Log > tab User Action
13. Verifikasi Activity Log bertambah tepat satu entri dibanding baseline (Edit Status Old Value `Active`, New Value `Inactive`)

### TC-FA-CAID-329: Surface sesi lain menampilkan konfigurasi baru tanpa menimpa form yang sedang diubah

14. Atur konfigurasi Company Alpha ke baseline B1 (seed API); di sesi 1 buka Fixed Asset > Settings > Asset Master > Custom Asset ID; di sesi 2 buka Fixed Asset > Settings > Asset Master > Custom Asset ID tanpa menyentuh form; di sesi 3 buka Fixed Asset > Assets > All Assets pada satu tab dan Fixed Asset > Settings > Asset Master > Custom Asset ID dengan Modal Changelog: Custom Asset ID terbuka pada tab lain
15. Di sesi 1 pilih Separator `- (Dash)`, lalu klik `[Save]`
16. Tunggu sampai nilai baru tampil di sesi 2 dan sesi 3 tanpa memuat ulang halaman (batas tunggu 10 detik)
17. Verifikasi sesi 3 menampilkan Asset ID baru berformat Dash di daftar aset tanpa dialog
18. Verifikasi sesi 3 menampilkan entri Edit Separator baru di Modal Changelog tanpa dialog
19. Verifikasi sesi 2 yang belum disentuh menampilkan Separator `- (Dash)` terbaru
20. Di sesi 2 pilih Separator `_ (Underscore)`
21. Di sesi 1 pilih Separator `. (Dot)`, lalu klik `[Save]`
22. Tunggu 5 detik tanpa memuat ulang halaman
23. Verifikasi sesi 3 menampilkan Asset ID berformat Dot di daftar aset
24. Verifikasi form sesi 2 tidak ditimpa dan tetap menampilkan Separator `_ (Underscore)`
25. Di sesi 2 kembalikan Separator ke nilai tersimpan `. (Dot)`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (seed baseline, membuka halaman, dan baseline jumlah entri, S-12) dan langkah 14 (seed baseline dan membuka halaman, termasuk tab Custom Asset ID di sesi 1 karena sesi 1 berakhir di Activity Log pada TC-FA-CAID-328), langkah 5 (muat ulang pada form pristine), langkah 6 dan 8 (membuka halaman), langkah 22 (jendela 5 detik sebelum asersi absence propagasi), dan langkah 25 (pemulihan form dirty sesi 2, S-09).
- Langkah 23 ditambahkan sebagai anchor positif untuk langkah 24 (bagian 8b butir 2): perubahan sesi 1 sudah tersebar ke sesi 3 sehingga form sesi 2 yang tidak berubah bukan karena propagasi belum terjadi.
- Langkah 7 dan 9 sampai 13 memeriksa "tanpa mass update kedua" lewat Asset ID dan jumlah entri tepat satu per surface; TC tidak memberi langkah observasi lain.
- Pembagian TC lintas spec: TC-FA-CAID-324, TC-FA-CAID-326, dan TC-FA-CAID-327 ada di spec 044.
- Temuan untuk QA:
  - TC-FA-CAID-329 langkah 3 meminta sesi 2 memilih `_ (Underscore)` "lebih dulu sebelum perubahan sesi 1 tiba" yang tidak dapat dijalankan sesudah langkah 2 (perubahan sesi 1 sudah tiba di sesi 2). Expected b (sesi 2 belum disentuh menampilkan Dash) dan Expected c (form sesi 2 tidak ditimpa) menuntut dua keadaan sesi 2 yang berbeda. Spec menjalankan b lebih dulu, lalu c lewat Save kedua di sesi 1 (Separator `. (Dot)`) sesudah sesi 2 memilih `_ (Underscore)`; QA diminta memastikan urutan ini.
  - TC-FA-CAID-329 Precondition d menyatakan sesi 1 sudah berada di tab Custom Asset ID, sedangkan TC-FA-CAID-328 sebelumnya meninggalkan sesi 1 di Activity Log; spec menambahkan pembukaan tab itu di sesi 1 pada langkah 14 sebelum Save langkah 15.
  - TC-FA-CAID-329 menempatkan sesi 3 pada akun Pre-setup No 1, akun yang sama dengan sesi 1; bila batas satu sesi web per akun berlaku, sesi 1 terusir. Kemampuan konteks browser ketiga untuk akun itu disediakan tim FE.
  - TC-FA-CAID-329 menyebut sesi 3 membuka All Assets dan Modal Changelog tanpa menyebut dua tab; spec memakai dua tab pada konteks yang sama.
  - TC-FA-CAID-329 tidak menyebut durasi untuk asersi "tidak ditimpa"; spec memakai jendela 5 detik (Prerequisites).
  - TC-FA-CAID-328 Expected b menyebut "tanpa mass update kedua" tanpa cara observasi terpisah; diasersi lewat Asset ID dan jumlah entri.
  - Post Condition TC-FA-CAID-328 dan TC-FA-CAID-329 tidak diasersi karena TC tidak memberi langkah observasinya.
