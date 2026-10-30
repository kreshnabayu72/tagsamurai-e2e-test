---
id: TC-GS-DIV-E2E-079-mobile-screening-card-list-row-action-dan-bottom-sheet
title: "Mobile: Screening Halaman, Card List, Row Action, dan Bottom Sheet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-281
  - TC-GS-DIV-282
  - TC-GS-DIV-283
  - TC-GS-DIV-284
coverage:
  mobile: automated
---

# Mobile: Screening Halaman, Card List, Row Action, dan Bottom Sheet

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android uji bersama, sehingga suite berjalan serial (`parallel: false`, S-09).
- Akun yang diuji (spec memakai dua akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | Read Only (Maya Putri) | `readOnly_automated_qaTeam1@qwertysystem.net` | `GS_RO_PASSWORD` |

  Login akun 1 di hook `before` spec ini pada aplikasi Android; hook `after` mengembalikan sesi ke akun default suite (akun 1). Halaman awal: aplikasi terbuka sebagai Total Control.
- Environment variable: `GS_TC_PASSWORD`, `GS_RO_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix `{runId}`): Division `Finance` (FIN), `Human Resources` (HR), `Legal` (LGL), `Operations` (OPS), `Compliance` (CMP), `Treasury` (TRS); `Finance` dipakai sebagai card acuan row action. Spec tidak membuat data (form Create hanya dibuka dan ditutup dalam keadaan kosong).
- Kemampuan teknis: gesture tap dan scroll horizontal, pembukaan serta penutupan bottom sheet di perangkat atau emulator Android, dan membaca format tanggal General Settings (untuk memeriksa tanggal Last Updated pada card).
- Tidak ada state global yang diubah.
- TC-GS-DIV-281, 282, 284: login sebagai Total Control. TC-GS-DIV-283: Total Control lalu Read Only. Semua pada aplikasi Android.

## Test Steps

### TC-GS-DIV-281: Screening halaman Division pada aplikasi mobile

1. Buka Global Settings > User > Division di aplikasi Android
2. Verifikasi Breadcrumb `User > Division`
3. Verifikasi Sub-Tabs Bar horizontal dan dapat di-scroll
4. Verifikasi Sub-Tabs Bar memuat `User List | Position | Division | Custom Field`
5. Verifikasi sub-tab `Division` aktif
6. Verifikasi Mobile Toolbar memuat icon `[⋯]` (bottom sheet)
7. Verifikasi Mobile Toolbar memuat icon `[🔍]` (inline search)
8. Verifikasi tombol `[+ Division]` terlihat di bawah toolbar dan di atas card list
9. Verifikasi Name pada tiap card Division ditampilkan tebal
10. Verifikasi tiap card Division memuat `[⋯]`
11. Verifikasi tiap card Division memuat Code, diikuti `·` dan Last Updated (contoh card `Finance` memuat `FIN`)
12. Verifikasi tanggal Last Updated pada card mengikuti format tanggal General Settings

### TC-GS-DIV-282: Card list mobile tanpa checkbox dan tanpa bulk action

13. Perhatikan card list pada Tab Division
14. Verifikasi tidak ada checkbox seleksi pada card
15. Verifikasi tidak ada Bulk Action Bar

### TC-GS-DIV-284: Toolbar, Filter, dan dialog mobile tampil sebagai bottom sheet

16. Ketuk `[⋯]` pada toolbar
17. Verifikasi bottom sheet `[⋯]` memuat Column Visibility, Filter, Download, dan Changelog
18. Ketuk `Filter`
19. Verifikasi Filter Panel tampil sebagai bottom sheet
20. Tutup bottom sheet Filter Panel hingga kembali ke daftar Division
21. Ketuk `[+ Division]`
22. Verifikasi form Create Division tampil sebagai bottom sheet
23. Tutup bottom sheet form Create Division (form kosong, tanpa perubahan)

### TC-GS-DIV-283: Row action card mobile mengikuti gating capability

24. Ketuk `[⋯]` pada card `Finance` (login sebagai Total Control)
25. Verifikasi `[⋯]` memuat `Edit`
26. Verifikasi `[⋯]` memuat `Delete`
27. Tutup menu `[⋯]` pada card
28. Logout, lalu login sebagai Read Only (`readOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_RO_PASSWORD`
29. Buka Global Settings > User > Division di aplikasi Android
30. Verifikasi card `Finance` tampil pada card list
31. Verifikasi `[⋯]` tidak tampil pada card `Finance` karena `Edit` dan `Delete` Hidden

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Spec mobile Android (`coverage.mobile: automated`, tanpa `web`, mengikuti spec mobile suite Brand).
- Urutan TC di spec berbeda dari urutan sumber (281, 282, 284, 283): screening tanpa aksi (281, 282) lebih dulu, bottom sheet (284) sebelum row action, dan TC-GS-DIV-283 paling akhir karena memuat satu kali ganti akun ke Read Only (langkah 28); akun Total Control dipulihkan oleh hook `after`.
- Langkah 1 TC-GS-DIV-282 ("Buka Tab Division") tidak ditulis ulang karena halaman Division sudah terbuka dari TC-GS-DIV-281 (langkah 13 hanya memperhatikan card list).
- Langkah 1 adalah Langkah Uji 1 TC-GS-DIV-281 ("Buka Global Settings > User > Division"), dan langkah 29 membuka ulang halaman sesudah ganti akun ke Read Only; keduanya sah dipertahankan (konvensi bagian 4).
- Langkah penghubung: langkah 29 (membuka halaman Division sesudah ganti akun); langkah 20 dan 23 (menutup bottom sheet Filter Panel dan form Create supaya TC berikutnya mulai dari daftar Division; form Create kosong tidak dirty, sehingga tidak ada dialog `Unsaved Changes`); langkah 27 (menutup menu `[⋯]` card).
- Expected Result a TC-GS-DIV-283 dipecah menjadi langkah 25 (`Edit`) dan 26 (`Delete`); Expected Result e TC-GS-DIV-281 dipecah menjadi langkah 9 sampai 12 (Name tebal, `[⋯]`, Code dan Last Updated, format tanggal).
- Asersi absence `[⋯]` pada langkah 31 didahului anchor positif langkah 30 (card `Finance` tampil pada card list yang sama; bagian 8b butir 2).
- Langkah 5 (sub-tab Division aktif) berasal dari penanda `(aktif)` pada Expected Result b TC-GS-DIV-281 dan dipisah dari urutan sub-tab (S-01).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-281: TC menyebut "tiap card" tetapi tidak menentukan card mana yang diperiksa; spec memeriksa semua card dengan `Finance` (FIN) sebagai contoh. Nilai Last Updated Division Pre-setup tidak disebut TC, sehingga tanggal hanya diperiksa terhadap format General Settings.
  - TC-GS-DIV-284: TC dan PRD §4.6 tidak menyebut cara menutup bottom sheet (tombol Back Android, swipe, atau `✕`) maupun apakah bottom sheet `[⋯]` tertutup otomatis saat `Filter` diketuk; langkah 20 dan 23 ditulis generik ("tutup bottom sheet") dan mekanismenya disediakan tim FE.
  - TC-GS-DIV-283: TC menulis "Login sbg Total Control: buka `[⋯]` pada card" tanpa menyebut card; spec memakai card `Finance`. Aktor ditulis `totalControl_automated`, `readOnly_automated` (tanpa domain); spec memakai email lengkap dari Tabel Data Uji Pre-setup.
  - TC-GS-DIV-282 dan 284 berstatus `UI Only` di TC sumber; sesuai bagian 2 konvensi tetap masuk spec.
