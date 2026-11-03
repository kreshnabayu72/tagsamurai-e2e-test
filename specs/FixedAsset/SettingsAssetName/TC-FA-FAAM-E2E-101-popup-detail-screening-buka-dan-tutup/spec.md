---
id: TC-FA-FAAM-E2E-101-popup-detail-screening-buka-dan-tutup
title: "Popup Detail: Screening, Buka dari Link dan Menu Aksi, dan Tutup Hanya Lewat [✕]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-302
  - TC-FA-FAAM-303
  - TC-FA-FAAM-304
coverage:
  web: automated
---

# Popup Detail: Screening, Buka dari Link dan Menu Aksi, dan Tutup Hanya Lewat [✕]

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca: Pre-setup #10 `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID` dan `QR`, Brand `Dell` model `3310`, `5420`, `7420`, UoM `Unit`, Total Asset 42), custom field Pre-setup #27 (3 Linked Custom Fields: `Cost Center`, `Operating System`, `Warranty Notes`), dan 42 aset Pre-setup #26; fixture `Fixture.faAssetName.dellLatitude`. Tidak ada data yang diubah.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-302: Screening Popup Detail Asset Name

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Verifikasi header berisi Title `Asset Name Detail` dan icon `[✕]` saja
4. Verifikasi tidak ada tombol `[Edit]` atau `[Close]` di footer
5. Verifikasi Identitas Utama berupa grid `Label: Value` 3 kolom dengan urutan Asset Name, Code, Category, TAG Type, UoM, Default Addon, Default Label
6. Verifikasi semua badge tampil penuh tanpa `+N more`
7. Verifikasi tab bar berurutan `Models per Brand (1)`, `Linked Custom Fields (3)`, `Total Assets (42)`
8. Verifikasi tab awal adalah `Models per Brand`
9. Klik tab `Linked Custom Fields (3)`
10. Verifikasi Identitas Utama tetap tampil di atas tab `Linked Custom Fields (3)`
11. Klik tab `Total Assets (42)`
12. Verifikasi Identitas Utama tetap tampil di atas tab `Total Assets (42)`

### TC-FA-FAAM-304: Popup Detail ditutup hanya lewat [✕], klik backdrop tidak menutup

13. Klik area gelap di luar popup
14. Verifikasi popup tidak menutup (Title `Asset Name Detail` tetap tampil)
15. Klik icon `[✕]`
16. Verifikasi popup menutup (Asset Name List tampil kembali)

### TC-FA-FAAM-303: Popup Detail dibuka dari link nama dan dari menu aksi Detail

17. Klik `⋯` baris `Dell Latitude` lalu `Detail`
18. Verifikasi Popup Detail yang sama terbuka: Title `Asset Name Detail`, Asset Name `Dell Latitude`, tab awal `Models per Brand`
19. Klik icon `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1), berpindah tab pada langkah 9 dan 11 (untuk mengamati Identitas Utama pada TC-FA-FAAM-302 Expected f), dan `[✕]` menutup popup (langkah 19).
- Urutan TC di dalam spec: TC-FA-FAAM-302, TC-FA-FAAM-304, lalu TC-FA-FAAM-303. Popup yang dibuka lewat link nama pada TC-FA-FAAM-302 (jalur pertama TC-FA-FAAM-303) dipakai lagi untuk TC-FA-FAAM-304 sehingga tidak dibuka-tutup tambahan; jalur kedua TC-FA-FAAM-303 (menu aksi `Detail`) dijalankan paling akhir dan dibandingkan dengan popup jalur pertama pada langkah 2 sampai 8.
- Asersi absence pada langkah 4 memakai header yang sudah diasersi pada langkah 3 sebagai anchor.
- Temuan untuk QA:
  - TC-FA-FAAM-302 Expected f ("Identitas Utama tetap tampil di atas semua tab") tidak punya langkah di TC; spec menambah langkah berpindah ke tab kedua dan ketiga (langkah 9 dan 11).
  - TC-FA-FAAM-303 Expected tidak menyebut apa yang membuat kedua jalur "sama"; spec membandingkan Title, Asset Name, dan tab awal.
