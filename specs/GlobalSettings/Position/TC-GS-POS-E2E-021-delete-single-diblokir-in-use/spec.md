---
id: TC-GS-POS-E2E-021-delete-single-diblokir-in-use
title: "Delete Position Tunggal Diblokir: Dipakai User Login, User Non-Login, atau Hanya User Non-Aktif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-114
  - TC-GS-POS-115
  - TC-GS-POS-116
  - TC-GS-POS-117
coverage:
  web: automated
---

# Delete Position Tunggal Diblokir: Dipakai User Login, User Non-Login, atau Hanya User Non-Aktif

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; langkah 1 tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tanpa suffix; spec ini tidak membuat, mengubah, atau menghapus data; Position in-use hanya menjadi target aksi Delete yang selalu diblokir guard, Last Updated tidak berubah):
  - Position 12 `Warehouse Supervisor`, dipakai user Login aktif `Rina Wulandari` (Pre-setup 17).
  - Position 13 `Customer Success Manager`, dipakai user Non-Login `Agus Pratama` (Pre-setup 17).
  - Position 14 `Procurement Officer`, hanya dipakai user Login non-aktif `Dewi Lestari` (Pre-setup 17).
- Data Dinamis: tidak ada.
- Cleanup: tidak ada data yang dibuat spec.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: Search tabel; pembacaan severity dan tipe tombol dialog.
- State global: tidak ada yang diubah spec ini selain flag Guided Tooltip yang diatur hook suite.

## Test Steps

### TC-GS-POS-114: Delete single, jabatan dipakai user Login diblokir

1. Ketik Search `Warehouse Supervisor`, tekan Enter
2. Klik `⋯` pada baris `Warehouse Supervisor`, pilih `Delete`
3. Verifikasi Dialog Delete Position tidak muncul
4. Verifikasi dialog blokir muncul dengan Title "Cannot Delete Data"
5. Verifikasi Header dialog berseverity warning
6. Verifikasi Body dialog menampilkan bullet `• Warehouse Supervisor`
7. Verifikasi Body dialog menampilkan teks "This position is still in use. Remove the references before deleting." di bawah bullet
8. Verifikasi Footer dialog hanya memiliki tombol tunggal `[OK]` bertipe text (contrast)

### TC-GS-POS-115: Dialog Cannot Delete Data, tombol OK

9. Klik `[OK]` pada dialog "Cannot Delete Data" yang terbuka dari langkah 2
10. Verifikasi tidak ada toast
11. Verifikasi dialog tertutup
12. Verifikasi baris `Warehouse Supervisor` tetap ada

### TC-GS-POS-116: Delete single, jabatan dipakai user Non-Login diblokir

13. Ganti isi kotak search dengan `Customer Success Manager`, tekan Enter
14. Klik `⋯` pada baris `Customer Success Manager`, pilih `Delete`
15. Verifikasi dialog "Cannot Delete Data" muncul
16. Verifikasi Body dialog menampilkan bullet `• Customer Success Manager`
17. Verifikasi Footer dialog menampilkan `[OK]`
18. Klik `[OK]`

### TC-GS-POS-117: Delete single, jabatan hanya dipakai user non-aktif

19. Ganti isi kotak search dengan `Procurement Officer`, tekan Enter
20. Klik `⋯` pada baris `Procurement Officer`, pilih `Delete`
21. Verifikasi dialog "Cannot Delete Data" muncul
22. Verifikasi Header dialog berseverity warning
23. Verifikasi Body dialog menampilkan bullet `• Procurement Officer`
24. Verifikasi Body dialog menampilkan teks "This position is still in use. Remove the references before deleting." di bawah bullet
25. Verifikasi Footer dialog hanya memiliki tombol tunggal `[OK]`
26. Klik `[OK]`
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: 114, 115, 116, 117. Dialog yang dibuka pada langkah 2 dipakai bersama TC-GS-POS-114 dan TC-GS-POS-115 (langkah 1 kedua TC identik), sehingga langkah 9 menutupnya dengan `[OK]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 13, dan 19 (Search agar baris target tampil di halaman aktif pada tabel 10 per halaman), langkah 18 dan 26 (menutup dialog dengan `[OK]` sebelum kasus berikutnya), serta langkah 27 (menutup input Search lewat `(←)`).
- Pada TC-GS-POS-115, asersi tidak ada toast (langkah 10) diletakkan segera sesudah klik `[OK]` dan sebelum asersi dialog tertutup dan baris tetap ada, karena toast adalah state sementara; urutan ini menyimpang dari urutan Expected TC (bagian 8b butir 5 dan 11).
- Seluruh kasus memakai data Pre-setup yang hanya dibaca (Delete diblokir, tidak ada perubahan data), sehingga tidak ada seeding, cleanup, atau suffix. Position Pre-setup 12, 13, dan 14 dirancang TC untuk kasus blokir; memakainya sebagai target Delete yang diblokir guard sah menurut pengecualian S-06 (hanya dibaca, tidak diubah).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi: "Tidak ada entri Changelog" (TC-GS-POS-115) dan "Record tetap ada" (TC-GS-POS-116 dan 117). Untuk TC-GS-POS-114 dan 115, baris tetap ada diasersi dari Expected TC-GS-POS-115 b.
  - TC-GS-POS-114 Expected a menyebut "Dialog Delete Position tidak muncul"; spec mengasersinya sebagai langkah tersendiri sebelum verifikasi isi dialog blokir.
