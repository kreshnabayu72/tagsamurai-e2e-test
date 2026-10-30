---
id: TC-GS-HHR-E2E-001-screening-tabel-layout-urutan-default-dan-kontras
title: "Screening Halaman Handheld Reader: Layout Tiga Zona, Urutan Default Device Name A-Z, Navigasi Keyboard Row Action, dan Kontras Teks WCAG 4.5:1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-1
  - TC-GS-HHR-2
  - TC-GS-HHR-463
  - TC-GS-HHR-464
coverage:
  web: automated
---

# Screening Halaman Handheld Reader: Layout Tiga Zona, Urutan Default Device Name A-Z, Navigasi Keyboard Row Action, dan Kontras Teks WCAG 4.5:1

## Prerequisites

- Mode: FE+BE (backend nyata). Suite `parallel: false`.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Hardware > Handheld Reader untuk akun Total Control; spec ini tidak menguji navigasi sidebar sehingga tidak mengulang langkah buka.
- Guided Tooltip: flag halaman Handheld Reader (`guided_tooltip_seen_gs-handheld-reader`) mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Client A, plan Growth, toggle BYO aktif, General Settings `dd/MM/yy` 24-hour Asia/Jakarta): Seed Reader A (DD-01 s.d. DD-10) dipulihkan fixture backend (disediakan tim FE) sebelum spec berjalan. Spec hanya membaca dan membuka lalu menutup Popup Detail, Dialog Edit Alias Name, dan Overlay row action tanpa menyimpan, sehingga data Seed Reader A tidak berubah.
- Peta baris Seed Reader A yang dipakai langkah:

| ID | Device Name | Serial Number | Status |
|---|---|---|---|
| DD-01 | `Zebra RFID Reader - 1` | `SN-HHR-00101` | Available |
| DD-02 | `Gudang Reader - 1` | `SN-HHR-00102` | Available |
| DD-05 | `Chainway C72 - 1` | `SN-HHR-00105` | Waiting for Approval |
| DD-06 | `Zebra RFID Reader - 1` | `SN-HHR-00107` | Available |
| DD-10 | `Gudang Reader - 4` | `SN-HHR-00205` | Waiting for Approval |

- Data Dinamis: tidak ada.
- Kemampuan teknis: hover; fokus keyboard (Tab, Enter, ArrowDown, Esc); pembacaan state disabled checkbox; pemeriksa kontras otomatis (aturan color-contrast WCAG 2.1 AA, misalnya axe atau setara) yang dapat dijalankan pada halaman, popup, dan dialog (TC-GS-HHR-464).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### TC-GS-HHR-1: Screening halaman Handheld Reader pada Client A

1. Amati header, License Counter Cards, toolbar, tabel, dan pagination dari atas ke bawah tanpa mengisi atau mengklik apa pun
2. Verifikasi Zona Header: Breadcrumb `Hardware > Handheld Reader`
3. Verifikasi Zona Header: tidak ada Page Title terpisah di bawah Breadcrumb
4. Verifikasi Zona Header: ikon `[?]` tepat di kanan Breadcrumb
5. Verifikasi Zona Header: License Counter Cards `Short Range` dan `Long Range` tampil
6. Verifikasi Zona Header: Table Tools `Search | Filter | Download | Changelog | Event Log | + Activate Reader` tampil
7. Verifikasi Zona Body: kolom tampil default `Checkbox (unsortable) | Device Name (sortable) | Alias Name (sortable) | Serial Number (sortable) | SKU (sortable) | Range Type (sortable) | Reader Power (sortable) | Source (sortable) | Last Scanned (sortable) | Status (sortable) | Column Visibility (⋯) (unsortable)`
8. Verifikasi Zona Body: kolom `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, dan `Activated At` tidak tampil
9. Verifikasi Zona Body: kolom `Checkbox` tampil sebagai kolom pertama dengan checkbox header dan satu checkbox per baris
10. Verifikasi Zona Body: checkbox baris `Chainway C72 - 1` (DD-05) dan `Gudang Reader - 4` (DD-10) disabled
11. Arahkan kursor ke checkbox baris `Chainway C72 - 1` (DD-05)
12. Verifikasi tooltip `This device is waiting for approval.`
13. Arahkan kursor ke checkbox baris `Gudang Reader - 4` (DD-10)
14. Verifikasi tooltip `This device is waiting for approval.`
15. Pindahkan kursor keluar dari tabel
16. Verifikasi Zona Body: Bulk Action Bar belum tampil karena belum ada baris tercentang
17. Verifikasi Zona Body: 10 baris tampil
18. Verifikasi Zona Footer: pagination menampilkan `Showing 1 - 10 of 10 readers`
19. Verifikasi Zona Footer: pagination menampilkan `Rows per page: 10`

### TC-GS-HHR-2: Urutan default Device Name A-Z dengan pembeda Serial Number untuk dua reader bernama sama

20. Amati urutan 10 baris dan indikator sort pada header kolom tanpa menyentuh header sort
21. Verifikasi urutan baris dari atas: `Chainway C72 - 1`, `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`, `Honeywell CK65 - 1`, `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1`, `Unitech EA520 - 1`, `Zebra Mobile Reader - 1`, `Zebra RFID Reader - 1` (`SN-HHR-00101`), `Zebra RFID Reader - 1` (`SN-HHR-00107`)
22. Verifikasi header kolom `Device Name` menampilkan indikator netral (urutan default tabel, bukan hasil klik sort)
23. Verifikasi dua baris `Zebra RFID Reader - 1` berurutan menurut Serial Number ascending: `SN-HHR-00101` lalu `SN-HHR-00107`

### TC-GS-HHR-463: Navigasi keyboard pada tabel dan Overlay row action

24. Tekan `Tab` hingga fokus berada pada ikon `(⋯)` baris `Zebra RFID Reader - 1` (`SN-HHR-00101`, DD-01)
25. Tekan `Enter`
26. Verifikasi `Enter` pada ikon `(⋯)` membuka Overlay row action DD-01
27. Tekan `ArrowDown` hingga fokus berada pada opsi `Detail`
28. Verifikasi `ArrowDown` memindahkan fokus antar opsi overlay menurut urutan opsi Overlay row action (PRD §4.2d)
29. Tekan `Enter`
30. Verifikasi `Enter` pada opsi `Detail` membuka Popup `Handheld Reader Detail` DD-01
31. Tekan `Esc`
32. Verifikasi `Esc` menutup Popup Detail

### TC-GS-HHR-464: Kontras teks halaman Handheld Reader memenuhi WCAG 2.1 AA 4.5:1

33. Jalankan pemeriksaan kontras otomatis (aturan color-contrast WCAG 2.1 AA) pada halaman
34. Verifikasi halaman tidak memiliki teks dengan rasio kontras di bawah 4.5:1
35. Klik Device Name `Zebra RFID Reader - 1` (`SN-HHR-00101`, DD-01) untuk membuka Popup Detail
36. Jalankan pemeriksaan kontras otomatis yang sama pada Popup Detail DD-01
37. Verifikasi Popup Detail tidak memiliki teks dengan rasio kontras di bawah 4.5:1
38. Tutup Popup Detail dengan `Esc`
39. Klik `(⋯)` baris `Gudang Reader - 1` (`SN-HHR-00102`, DD-02), lalu klik `Edit Alias Name`
40. Jalankan pemeriksaan kontras otomatis yang sama pada Dialog Edit Alias Name DD-02
41. Verifikasi Dialog Edit Alias Name tidak memiliki teks dengan rasio kontras di bawah 4.5:1
42. Tutup Dialog Edit Alias Name dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 1, 2, 463, 464. TC-GS-HHR-1 dan 2 ditaruh paling awal karena menguji keadaan awal tabel (urutan default tanpa sort) sebelum langkah apa pun yang mengubah state; TC-GS-HHR-464 membuka Popup Detail dan Dialog Edit Alias Name sebagai kejadian terakhir. Dialog Edit Alias Name dibuka satu kali dan ditutup satu kali tanpa mengubah isi (form bersih, tidak memunculkan `Unsaved Changes`).
- Pembukaan Global Settings > Hardware > Handheld Reader dilakukan hook `beforeEach`; langkah "Buka Global Settings > Hardware > Handheld Reader" pada TC-GS-HHR-1, 2, dan 464 tidak diulang.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 (memindahkan kursor), langkah 35 (membuka Popup Detail lewat klik Device Name sebagai cara membuka popup pada TC-GS-HHR-464 karena TC tidak menyebut caranya), langkah 38 (menutup Popup Detail), langkah 39 (membuka Dialog Edit Alias Name lewat row action) dan langkah 42 (menutup dialog).
- Verifikasi tooltip checkbox DD-05 dan DD-10 (langkah 11 sampai 14) memetakan Expected b.iii TC-GS-HHR-1; TC hanya menyebut tooltip tanpa langkah hover, sehingga langkah hover (langkah 11 dan 13) ditulis sebagai aksi pemicu tooltip.
- Spec melewati sekitar 35 langkah (42 langkah). Seluruhnya satu kelas (screening baca halaman utama Handheld Reader tanpa aksi yang mengubah data), tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; pemeriksa kontras (TC-GS-HHR-464) berada paling akhir dan tidak dipakai blok lain.
- Temuan untuk QA:
  - TC-GS-HHR-1 Expected b.i menamai kolom terakhir `Column Visibility (⋯)`, sedangkan TC-GS-HHR-5 dan 8 menamainya `Actions (⋯)` dan TC-GS-HHR-277 menyebut tooltip header `Column Visibility`. Spec mengikuti penamaan masing-masing TC.
  - TC-GS-HHR-463 Expected b merujuk urutan opsi pada PRD §4.2d tanpa menuliskan urutan opsinya di TC; spec mengasersi bahwa fokus berpindah antar opsi menurut urutan PRD tanpa mengarang daftar opsi.
  - TC-GS-HHR-463 tidak menyebut apakah fokus awal Overlay row action sudah berada pada opsi `Detail`; spec menekan `ArrowDown` hingga `Detail` fokus.
  - TC-GS-HHR-464 tidak menyebut alat pemeriksa kontras; kemampuan teknis ditulis di Prerequisites (axe atau setara) dan dilengkapi tim FE.
  - TC-GS-HHR-464 tidak menyebut cara membuka Popup Detail DD-01 dan Dialog Edit Alias Name DD-02; spec memakai klik Device Name dan row action `Edit Alias Name`.
