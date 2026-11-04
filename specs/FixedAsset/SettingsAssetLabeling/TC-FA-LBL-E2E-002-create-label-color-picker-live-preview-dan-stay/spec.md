---
id: TC-FA-LBL-E2E-002-create-label-color-picker-live-preview-dan-stay
title: "Create Label: Color Picker, Live Preview, dan checkbox Stay on this form"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:FI-02
  - FALB:FI-03
  - FALB:FI-04
  - FALB:FI-05
  - FALB:FI-06
  - FALB-LOGIC-03a
coverage:
  web: automated
---

# Create Label: Color Picker, Live Preview, dan checkbox Stay on this form

## Prerequisites

- Mode: FE+BE
- Akun: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-09` (swatch preset pertama `#EF4444` dan titik kanvas = klik di tengah Kanvas Warna Kustom, 50% lebar dan 50% tinggi), `DU-10` (kode hex valid yang diketik di kolom Hex), `DU-11` (nama label uji Live Preview, bersuffix `{runId}-002`).
- Hex titik kanvas bergantung pada implementasi komponen kanvas: langkah 10 mengasersi kolom Hex berformat `#RRGGBB` dan berbeda dari `#EF4444`, lalu mencatat nilainya sebagai hex kanvas yang dipakai langkah 11 dan 15.
- Spec ini tidak menyimpan label: form selalu ditutup tanpa Submit (langkah 26 sampai 28), sehingga tidak membuat data dan tidak butuh cleanup.

## Test Steps

### FALB:FI-06: Checkbox Stay on this form after submitting tampil pada mode Create

1. Klik `[+ Label]`
2. Verifikasi Modal Create Label tampil dengan judul `Create Label`
3. Verifikasi checkbox `Stay on this form after submitting` tampil di footer Modal Create Label

### FALB:FI-02: Klik swatch membuka Color Picker Overlay

4. Klik Swatch Trigger pada field Color
5. Verifikasi Color Picker Overlay tampil

### FALB:FI-03: Memilih warna lewat swatch preset atau kanvas

6. Klik swatch preset pertama (`#EF4444`, `DU-09`) pada palet preset
7. Verifikasi kolom Hex berisi `#EF4444`
8. Verifikasi Swatch Trigger memakai warna `#EF4444`
9. Klik titik tengah kanvas warna kustom (`DU-09`)
10. Verifikasi kolom Hex berisi kode `#RRGGBB` 6 digit yang berbeda dari `#EF4444`, catat sebagai hex kanvas
11. Verifikasi Swatch Trigger memakai warna hex kanvas yang dicatat pada langkah 10

### FALB:FI-04: Escape menutup overlay tanpa menutup modal form

12. Tekan Esc
13. Verifikasi Modal Create Label masih tampil
14. Verifikasi Color Picker Overlay tidak tampil

### FALB:FI-05: Live Preview mengikuti nama dan warna

15. Verifikasi section Live Preview memuat caption `Live Preview` dan chip badge berlatar hex kanvas yang dicatat pada langkah 10
16. Ketik Label Name `DU-11`
17. Verifikasi chip Live Preview menampilkan teks `DU-11`
18. Klik Swatch Trigger pada field Color
19. Klik swatch preset pertama (`#EF4444`, `DU-09`) pada palet preset
20. Verifikasi chip Live Preview berlatar `#EF4444` dan tetap menampilkan teks `DU-11`
21. Tekan Esc

### FALB-LOGIC-03a: Warna berformat #RRGGBB

22. Klik Swatch Trigger pada field Color
23. Ketik di kolom Hex kode `DU-10`
24. Verifikasi kolom Hex berisi kode berformat `#` diikuti 6 digit heksadesimal sesuai `DU-10`
25. Tekan Esc
26. Klik `[✕]` pada header Modal Create Label
27. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1, 21, 22, 25, 26, dan 28. Langkah 26 sampai 28 menutup form dirty secara deterministik (S-08) dan membuang isian tanpa menyimpan.
- Anchor positif (bagian 8b butir 2): langkah 2 membuktikan Modal Create Label sudah terbuka sebelum asersi checkbox di langkah 3 dan sebelum absence overlay di langkah 14; langkah 13 membuktikan modal masih tampil sebelum langkah 14.
- Pembagian klausa lintas spec: klausa pertama `FALB:FI-06` (checkbox hanya tampil pada mode Create) diasersi di spec ini pada form Create; klausa bahwa checkbox tidak tampil pada mode Edit ada di spec 008.
- Pembagian klausa lintas spec: `FALB:FI-05` dan `FALB:FI-03` memakai kolom Hex, Swatch Trigger, dan Live Preview pada form yang sama; Live Preview diasersi di langkah 15, 17, dan 20 untuk `FALB:FI-05`, sedangkan langkah 8 dan 11 untuk `FALB:FI-03` hanya mengasersi Swatch Trigger.
- Temuan PRD / aturan ditahan: isi tepat 16 swatch palet preset adalah klausa aturan `FALB-LOGIC-03b` yang ditahan, dan tampilan huruf kapital pada kolom Hex adalah klausa aturan `FALB:FI-09` yang ditahan; keduanya tidak diasersi.
- Temuan PRD: PRD §4.3 (Color Picker Overlay, Kolom Hex, Perilaku Tutup, dan Live Preview Section) menyatakan perilaku berikut dalam teks tanpa ID leaf sendiri, sehingga tidak diasersi: kontras otomatis teks chip Live Preview putih atau hitam menurut WCAG 2.1 (aturan terdekat `FALB:FI-05`) dan overlay tetap terbuka setelah memilih swatch, titik kanvas, atau mengetik kode (aturan terdekat `FALB:FI-03`).
- Kode `DU-10` diketik apa adanya; langkah 24 hanya mengasersi format `#RRGGBB`, bukan tampilan huruf besar atau kecil.
- Isi dialog `Unsaved Changes` mengikuti konvensi platform, bukan PRD modul; spec hanya mengasersi judul dan tombolnya.
