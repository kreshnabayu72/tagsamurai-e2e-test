---
id: TC-FA-FAAM-E2E-104-popup-detail-retensi-state-tab-total-assets
title: "Popup Detail: Pindah Tab Memulihkan State Tab Total Assets dan Buka Ulang Mereset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-315
  - TC-FA-FAAM-316
coverage:
  web: automated
---

# Popup Detail: Pindah Tab Memulihkan State Tab Total Assets dan Buka Ulang Mereset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca: Pre-setup #10 `Dell Latitude` dengan 42 aset (`Dell Latitude - 1` sampai `Dell Latitude - 42`, Pre-setup #26) sehingga hasil Search `Dell` dengan Filter Brand `Dell` berisi lebih dari satu halaman; Pre-setup #14 `Service Vehicle` (Total Asset 8). Fixture `Fixture.faAssetName.dellLatitude`. Tidak ada data yang diubah.
- Data uji: Search `Dell`, Filter Brand `Dell`.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah. Retensi state tab hanya hidup selama popup terbuka dan tidak dipersistensikan.

## Test Steps

### TC-FA-FAAM-315: Pindah tab Popup Detail memulihkan state Tab Total Assets

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Buka tab Total Assets, ketik `Dell` di Search lalu Enter
4. Klik Filter, pilih Brand `Dell`, klik `[Apply]`
5. Klik header Name
6. Pindah ke halaman 2
7. Pindah ke tab Models per Brand lalu kembali ke tab Total Assets
8. Verifikasi Search berisi `Dell`
9. Verifikasi Filter Brand `Dell` tetap ter-Apply
10. Verifikasi Sort Name tetap aktif
11. Verifikasi halaman 2 tetap aktif

### TC-FA-FAAM-316: Menutup dan membuka ulang Popup Detail mereset ke default

12. Klik icon `[✕]` untuk menutup popup
13. Klik nama `Dell Latitude`
14. Verifikasi tab awal adalah `Models per Brand`
15. Klik tab Total Assets
16. Verifikasi Search kosong
17. Verifikasi Filter kosong
18. Verifikasi halaman 1 aktif
19. Verifikasi Sort Last Updated Newest First aktif
20. Ketik `Dell` di Search lalu Enter
21. Pindah ke halaman 2
22. Klik icon `[✕]` untuk menutup popup
23. Ganti isi kotak search dengan `Service Vehicle`, tekan Enter
24. Klik nama `Service Vehicle`
25. Verifikasi tab awal adalah `Models per Brand`
26. Klik tab Total Assets
27. Verifikasi Search kosong
28. Verifikasi Filter kosong
29. Verifikasi halaman 1 aktif
30. Verifikasi Sort Last Updated Newest First aktif
31. Klik icon `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 23) dan `[✕]` menutup popup (langkah 12, 22, 31).
- Langkah pembuka TC-FA-FAAM-316 (membuka popup, mengisi Search, Filter, dan halaman 2) identik dengan langkah 2 sampai 6 milik TC-FA-FAAM-315; state yang sudah terbentuk pada langkah 7 dipakai sebagai state yang harus direset oleh langkah 12 sampai 19, tanpa mengulang pengisiannya. Pengisian ulang Search dan halaman 2 sebelum menutup popup untuk Asset Name lain (langkah 20 sampai 22) adalah langkah TC-FA-FAAM-316 yang berikutnya.
- Temuan untuk QA:
  - TC-FA-FAAM-315 mengandaikan hasil Search `Dell` dengan Filter Brand `Dell` memiliki lebih dari satu halaman; Pre-setup #26 tidak menyebut Brand tiap aset, sehingga spec mengandalkan 42 aset `Dell Latitude - n` ber-Brand `Dell`.
  - TC-FA-FAAM-316 Expected a.ii dan b.ii menyebut "Sort Last Updated Newest First" sebagai default tanpa menyebut indikator UI-nya; spec mengasersi sort aktif pada kolom Last Updated dengan urutan terbaru lebih dulu.
