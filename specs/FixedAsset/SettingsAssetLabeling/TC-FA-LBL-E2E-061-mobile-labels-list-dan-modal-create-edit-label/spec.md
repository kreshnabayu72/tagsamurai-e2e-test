---
id: TC-FA-LBL-E2E-061-mobile-labels-list-dan-modal-create-edit-label
title: "Mobile: Labels List sebagai Card List dan Modal Create/Edit Label full-screen"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:mobile-layout/labels-list
  - FALB:mobile-layout/modal-create-edit-label
coverage:
  mobile: automated
---

# Mobile: Labels List sebagai Card List dan Modal Create/Edit Label full-screen

## Prerequisites

- Mode: FE+BE (backend nyata). Platform: aplikasi native Android (PRD §4.8 Mobile Layout); Labels List tampil sebagai Card List.
- Perangkat atau emulator Android dengan aplikasi TAG Samurai terpasang (`DU-66`), serta kemampuan mengetuk elemen UI, menggulir layar, dan membaca isi Card List; disediakan tim FE. Spec ini hanya berjalan di aplikasi mobile (`coverage.mobile: automated`). `parallel: false` untuk perangkat bersama.
- Akun aktor pertama: Read Only (`DU-02`), env `FA_RO_EMAIL` dan `FA_RO_PASSWORD`, login di aplikasi pada hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Ganti akun eksplisit ke Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD` (langkah 9). Hook `after` mengembalikan sesi ke akun default suite (`DU-01`).
- Data uji `DU-56` (Dataset Labels List: 12 label bersuffix), pola `Lst-{runId}-061-nn`, dibuat lewat sesi API di hook `before` dan dihapus di hook `after`; satu Search `DU-56` menampilkan ke-12 card.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, aset, dan Modified By dari dua aktor, disediakan tim FE/BE.
- State global: tidak ada yang diubah; modal Create ditutup tanpa Submit dan Edit tanpa perubahan tidak menulis data. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:mobile-layout/labels-list: Labels List sebagai Card List per label

1. Ketik Search `DU-56`, tekan Enter
2. Verifikasi Labels List tampil sebagai Card List dengan satu card per label milik `DU-56`
3. Verifikasi card menampilkan chip badge label berlatar warna label (tebal)
4. Verifikasi card menampilkan Color Hex, Total Asset, dan Modified By · Last Updated
5. Verifikasi ikon `[⋯]` tidak tampil pada card Read Only karena tidak ada aksi yang diizinkan
6. Ketuk chip badge label pada card pertama
7. Verifikasi Drawer Tagged Asset tampil
8. Tutup Drawer Tagged Asset lewat `[✕]`
9. Ganti akun ke Total Control: logout di aplikasi, login dengan akun `DU-01`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
10. Ketik Search `DU-56`, tekan Enter
11. Verifikasi card label milik `DU-56` tampil dengan ikon `[⋯]`
12. Ketuk `[⋯]` pada card pertama
13. Verifikasi menu card memuat aksi `Edit` dan `Delete`
14. Tutup menu card
15. Ketuk `[⋯]` pada toolbar
16. Verifikasi bottom sheet toolbar memuat Filter dan Download tanpa Column Visibility
17. Tutup bottom sheet toolbar

### FALB:mobile-layout/modal-create-edit-label: Modal Create/Edit Label sebagai full-screen sheet satu kolom

18. Ketuk `[+ Label]` di bawah toolbar
19. Verifikasi Modal Create Label tampil sebagai full-screen sheet satu kolom
20. Ketuk Swatch Trigger
21. Verifikasi Color Picker Overlay (palet preset, kanvas kustom, dan kolom Hex) tampil penuh lebar di bawah Swatch Trigger
22. Verifikasi section Live Preview tampil di atas footer
23. Gulir form ke bawah
24. Verifikasi section Live Preview tetap tampil di atas footer setelah form digulir
25. Tutup modal lewat `[✕]`
26. Ketuk `[⋯]` pada card pertama, lalu ketuk `Edit`
27. Verifikasi Modal Edit Label tampil sebagai full-screen sheet satu kolom
28. Ketuk `[Save]` tanpa mengubah nama dan warna
29. Verifikasi toast `No changes to save.` tampil

## Notes

- Langkah penghubung (S-03): langkah 1 dan 10 mempersempit Card List ke label `DU-56` (R-16); langkah 8, 14, 17, dan 25 menutup drawer, menu, bottom sheet, dan modal; langkah 9 adalah langkah ganti akun eksplisit tanpa `Verifikasi` karena akun pertama login di hook `before`; langkah 12, 15, 18, 20, 23, dan 26 hanya membuka elemen.
- Anchor absence: langkah 2 sampai 4 (card tampil dengan chip, Color Hex, Total Asset, dan Modified By · Last Updated) mendahului asersi ikon `[⋯]` tidak tampil di langkah 5 (PRD §4.7: ikon `[⋯]` Hidden bila tidak ada aksi yang diizinkan, View Tagged Assets tetap tersedia lewat ketuk chip, langkah 6 sampai 7); langkah 11 membuktikan ikon `[⋯]` tampil bagi `DU-01`.
- Spec ini tidak mengasersi Submit Create; modal Create ditutup tanpa perubahan (langkah 25) sehingga tidak ada data yang dibuat atau dihapus. Aturan field mengikuti §4.3 dan validasi §6, yang diasersi di spec web suite ini.
