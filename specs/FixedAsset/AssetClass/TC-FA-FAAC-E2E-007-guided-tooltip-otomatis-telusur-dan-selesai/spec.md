---
id: TC-FA-FAAC-E2E-007-guided-tooltip-otomatis-telusur-dan-selesai
title: "Guided Tooltip Tab Asset Class: Mulai Otomatis pada Kunjungan Pertama, Telusur Delapan Step dengan Next, dan Done Menyimpan Flag"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-46
  - TC-FA-FAAC-47
  - TC-FA-FAAC-48
coverage:
  web: automated
---

# Guided Tooltip Tab Asset Class: Mulai Otomatis pada Kunjungan Pertama, Telusur Delapan Step dengan Next, dan Done Menyimpan Flag

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini. Pengecualian atas hook `beforeEach` dan hook suite: spec Guided Tooltip menguji kunjungan pertama dan membuka layarnya sendiri lewat sidebar; hook suite tidak menyetel flag `guided_tooltip_seen_fa-asset-class` true untuk spec ini, dan spec mengaturnya per blok (langkah 1, 12, dan 25). Hook `after` memulihkan flag ke nilai awal dan mengembalikan sesi ke akun default suite.
- Kemampuan teknis: mengatur dan memulihkan flag `guided_tooltip_seen_fa-asset-class` untuk akun Total Control; disediakan tim FE/BE (lihat `suite.md`).
- Jeda "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 4 dan 34) adalah pilihan spec sebagai jendela asersi absence, bukan nilai TC atau PRD.
- Tabel "Step Guided Tooltip" (TC-FA-FAAC-47, langkah 15 sampai 20):

| Step | Spotlight | Title | Description |
|---|---|---|---|
| 1 | tab bar halaman Accounting | `Set Up in Order` | `The tabs follow the order in which accounting is set up, from Preferences to Asset Class.` |
| 2 | header kolom Class Code | `Asset Class` | `Groups assets by their accounting rules. Assets follow the rules of the asset class assigned to their asset name.` |
| 3 | header kolom Commercial | `Commercial Depreciation` | `Shows how the asset class depreciates in your books.` |
| 4 | header kolom Fiscal | `Fiscal Depreciation` | `Shows the tax depreciation class the asset class uses.` |
| 5 | header kolom Accounts | `Accounts` | `Shows whether the accounts needed for journals are complete. Incomplete accounts hold journals at export, not asset operations.` |
| 6 | header kolom Asset Names | `Asset Names` | `Shows how many asset names use this asset class. Open it to assign or move asset names.` |
| 7 | icon Filter di toolbar | `Filter Asset Classes` | `Narrow down the list. Filters combine with your search.` |

- Suite berjalan serial (`parallel: false`) karena spec ini mengubah flag Guided Tooltip akun aktor.

## Test Steps

### TC-FA-FAAC-46: Walkthrough otomatis pada kunjungan pertama ke tab Asset Class

1. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
2. Klik menu Accounting di sidebar
3. Verifikasi tab `Preferences` aktif
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi Guided Tooltip `fa-asset-class` tidak dimulai selama tab `Preferences` aktif
6. Klik tab Asset Class
7. Verifikasi walkthrough dimulai otomatis dengan overlay gelap dan spotlight pada tab bar halaman Accounting
8. Verifikasi kotak tooltip menampilkan `Step 1 of 8`, Title `Set Up in Order`, dan Description `The tabs follow the order in which accounting is set up, from Preferences to Asset Class.` tanpa spasi di akhir teks
9. Verifikasi navigasi menampilkan link `[Skip]` dan tombol `[Next]`
10. Verifikasi tombol `[Back]` Hidden pada Step 1

### TC-FA-FAAC-47: Menelusuri kedelapan step dengan tombol Next

11. Klik menu Dashboard di sidebar
12. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
13. Klik menu Accounting di sidebar
14. Klik tab Asset Class
15. Untuk setiap step 1 sampai 7 pada tabel "Step Guided Tooltip", lakukan langkah 16 sampai 20
16. Verifikasi spotlight berada pada elemen yang tertulis di tabel
17. Verifikasi indikator `Step N of 8` sesuai nomor step di tabel
18. Verifikasi Title sesuai tabel
19. Verifikasi Description sesuai tabel
20. Klik `[Next]`
21. Verifikasi spotlight Step 8 of 8 berada pada icon Changelog di toolbar
22. Verifikasi Title Step 8 of 8 `Changelog`
23. Verifikasi Description Step 8 of 8 `See the history of changes made to asset classes.`

### TC-FA-FAAC-48: Step 8 menampilkan Done lalu menutup walkthrough dan menyimpan flag

24. Klik menu Dashboard di sidebar
25. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
26. Klik menu Accounting di sidebar
27. Klik tab Asset Class
28. Klik `[Next]` tujuh kali hingga Step 8 of 8
29. Verifikasi tombol `[Next]` berganti menjadi `[Done]` pada Step 8
30. Klik `[Done]`
31. Verifikasi walkthrough tertutup
32. Refresh halaman
33. Klik tab Asset Class
34. Tunggu 5 detik tanpa memuat ulang halaman
35. Verifikasi tab `Asset Class` aktif dengan tabel Asset Class tampil
36. Verifikasi walkthrough tidak muncul otomatis lagi

## Notes

- Spec melewati sekitar 35 langkah dengan ekspansi (36 langkah nominal; langkah 16 sampai 20 diulang tujuh kali): ketiga blok adalah satu kelas (Guided Tooltip fungsional) pada layar dan dataset yang sama, tiap blok memulai walkthrough sendiri, dan memisahnya hanya menggandakan login, hook, dan pemulihan flag. Perulangan memakai tabel di `## Prerequisites` (8b butir 7); `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03): langkah 1, 12, dan 25 (mengatur flag belum tersimpan sebagai precondition tiap TC), langkah 11 dan 24 (pindah halaman agar walkthrough yang berjalan tertutup tanpa menyimpan flag, perilaku TC-FA-FAAC-55), langkah 15 (perulangan), langkah 28 (`[Next]` tujuh kali ditulis satu langkah karena aksinya identik dan tanpa asersi), langkah 4 dan 34 (jendela asersi absence), langkah 32 dan 33 (muat ulang lalu buka tab sesuai TC).
- Perilaku asersi absence (langkah 5 dan 36): langkah 3 dan 35 menjadi anchor positif bahwa halaman sudah termuat sebelum absence walkthrough diasersi (8b butir 2, R-21).
- Temuan untuk QA:
  - TC-FA-FAAC-46 langkah 2 ("Perhatikan halaman beberapa saat") tidak menyebut durasi; spec memakai jendela 5 detik (bagian 6).
  - TC-FA-FAAC-48 Post Condition (flag tersimpan) tidak punya langkah observasi dan tidak diasersi terpisah; perilaku tersirat dari butir c.
