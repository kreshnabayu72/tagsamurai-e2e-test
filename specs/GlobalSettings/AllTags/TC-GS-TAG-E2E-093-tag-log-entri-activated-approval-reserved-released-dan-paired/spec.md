---
id: TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired
title: "TAG Log: Entri Activated, Waiting for Approval dan Approved, Reserved dan Released, serta Paired per Tipe Entitas (Termasuk Previous Status)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-277
  - TC-GS-TAG-278
  - TC-GS-TAG-279
  - TC-GS-TAG-280
  - TC-GS-TAG-369
coverage:
  web: automated
---

# TAG Log: Entri Activated, Waiting for Approval dan Approved, Reserved dan Released, serta Paired per Tipe Entitas (Termasuk Previous Status)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client Log Wulan Sari `totalControl_automated_qaLog@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_LOG_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Login sekali di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client Log (dibaca saja, tanpa aksi tulis; fixture TAG Log DD-39 sampai DD-59, Tabel Data Uji Dinamis TC, dibuat lewat fixture BE; mekanisme dan pelaku fixture disediakan tim FE/BE, lihat Temuan untuk QA):

| ID | Code | Riwayat yang diasersi |
|---|---|---|
| DD-39 | `E2801160600002054D8C0039` | `Activated` 16/09/26 14:30 oleh Budi Santoso dengan Handheld Reader `Zebra RFD40 (SN-2201)` |
| DD-40 | `E2801160600002054D8C0040` | `Activated` 16/09/26 14:35 oleh Budi Santoso tanpa reader |
| DD-41 | `04A224B2C15F41` | `Waiting for Approval` 10/09/26 09:00 oleh Budi Santoso; `Approved` 11/09/26 10:00 oleh approver (Approval Note `Verified with distributor`) |
| DD-42 | `E2801160600002054D8C0042` | `Reserved` 12/09/26 09:00 oleh Siti Amalia (aset `Forklift 01`, kode `AST-0042`); `Released` 12/09/26 15:00 oleh approver (Reason `Asset rejected`) |
| DD-43 | `E2801160600002054D8C0043` | `Activated` 08/09/26 08:00; `Paired` ke Asset `Forklift 01` (`AST-0043`) 09/09/26 10:00 oleh Budi Santoso, Module `Fixed Asset > Register Asset` (dipair langsung dari Available) |
| DD-44 | `E2801160600002054D8C0044` | `Activated` 08/09/26 08:05; `Paired` ke User `Siti Amalia` (Employee ID `EMP-0044`) 09/09/26 10:05 |
| DD-45 | `04A224B2C15F45` | `Activated` 08/09/26 08:10; `Paired` ke Supply Item `Safety Helmet` (`ITM-0045`) 09/09/26 10:10 |
| DD-59 | `E2801160600002054D8C0059` | `Activated`; `Paired` ke Asset; `To be Returned` (Reason `Disposal`, Return Group `Gudang Pusat`); `Paired` ke Asset lain lewat FAMS Pair TAG tanpa Receive, Previous Status `To be Returned` |

- Nama approver (DD-41, DD-42) dan pelaku pair DD-44, DD-45, DD-59, serta nilai `Module` DD-44, DD-45, DD-59, tidak disebut TC dan dibaca dari fixture (disediakan tim FE/BE; Q-15). Pelaku tampil sebagai `[First Name] [Last Initial]`: `Budi S` (Budi Santoso) dan `Siti A` (Siti Amalia).
- Kemampuan teknis: mengatur fixture TAG Log di atas pada Client Log; Search registri agar baris target tampil.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-TAG-277: Entri Activated, judul memuat nama admin Submit, Description Hardware hanya bila sesi memakai reader

1. Ketik Search `E2801160600002054D8C0039`, tekan Enter, buka menu baris DD-39, klik `TAG Log`
2. Verifikasi entri `TAG Activated by Budi S` memuat baris `Hardware: Zebra RFD40 (SN-2201)`
3. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `E2801160600002054D8C0040`, tekan Enter, buka menu baris DD-40, klik `TAG Log`
4. Verifikasi entri `TAG Activated by Budi S` tampil
5. Verifikasi entri `TAG Activated by Budi S` tidak memuat baris Description
6. Tutup popup lewat `[✕]`

### TC-GS-TAG-278: Entri Waiting for Approval dan Approved dengan Approval Note

7. Ganti isi kotak search dengan `04A224B2C15F41`, tekan Enter, buka menu baris DD-41, klik `TAG Log`
8. Verifikasi entri `TAG Sent for Approval by Budi S` tampil
9. Verifikasi entri `TAG Sent for Approval by Budi S` tidak memuat Description
10. Verifikasi entri `TAG Approved by` pelaku approver memuat baris `Approval Note: Verified with distributor`
11. Tutup popup lewat `[✕]`

### TC-GS-TAG-279: Entri Reserved dan Released dengan Reason Asset rejected

12. Ganti isi kotak search dengan `E2801160600002054D8C0042`, tekan Enter, buka menu baris DD-42, klik `TAG Log`
13. Verifikasi entri `TAG Reserved by Siti A` memuat `Asset` `Forklift 01` dan `Asset Code` `AST-0042`
14. Verifikasi entri `TAG Released by` pelaku approver memuat `Asset` `Forklift 01`, `Asset Code` `AST-0042`, dan `Reason: Asset rejected`
15. Tutup popup lewat `[✕]`

### TC-GS-TAG-280 dan TC-GS-TAG-369: Entri Paired per tipe entitas dan Previous Status

16. Ganti isi kotak search dengan `E2801160600002054D8C0043`, tekan Enter, buka menu baris DD-43, klik `TAG Log`
17. Verifikasi judul entri `TAG Paired by Budi S` tampil
18. Verifikasi entri Paired DD-43 memuat `Type: Asset`, `Asset` `Forklift 01`, `Asset Code` `AST-0043`, dan `Module` `Fixed Asset > Register Asset` (format sama dengan hover Last Scanned In)
19. Verifikasi entri `TAG Paired by Budi S` DD-43 tidak memuat baris `Previous Status` (dipair langsung dari Available)
20. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `E2801160600002054D8C0044`, tekan Enter, buka menu baris DD-44, klik `TAG Log`
21. Verifikasi judul entri `TAG Paired by` pelaku pair tampil
22. Verifikasi entri Paired DD-44 memuat `Type: User`, `Name` `Siti Amalia`, `Employee ID` `EMP-0044`, dan `Module`
23. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `04A224B2C15F45`, tekan Enter, buka menu baris DD-45, klik `TAG Log`
24. Verifikasi judul entri `TAG Paired by` pelaku pair tampil
25. Verifikasi entri Paired DD-45 memuat `Type: Supply Item`, `Supply Item` `Safety Helmet`, `Item Code` `ITM-0045`, dan `Module`
26. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `E2801160600002054D8C0059`, tekan Enter, buka menu baris DD-59, klik `TAG Log`
27. Verifikasi entri `TAG Paired by` pelaku pair DD-59 memuat `Type: Asset`, `Asset`, `Asset Code`, `Module`, dan `Previous Status: To be Returned`
28. Verifikasi entri `TAG Marked To be Returned by` sebelumnya tetap tampil
29. Verifikasi tidak ada entri `TAG Received by` pada TAG Log DD-59
30. Tutup popup lewat `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data.
- Urutan TC dalam spec: 277, 278, 279, 280 (bersama TC-369 butir b pada popup DD-43), 369 (DD-59). TC-369 langkah 2 membuka TAG Log DD-43 yang sudah dibuka untuk TC-280 langkah 1; asersi `Previous Status` tidak ada diletakkan di popup yang sama (langkah 19) agar tidak membuka ulang tanpa alasan state (prinsip "halaman yang sama dipakai berulang"). Perubahan urutan dicatat sesuai S-05.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 3, 7, 12, 16, 20, 23, 26 (Search agar baris target tampil dan membuka TAG Log), langkah 3, 6, 11, 15, 20, 23, 26, 30 (menutup popup).
- Langkah 5, 9, dan 29 (absence) memakai entri lain pada popup yang sama (langkah 4, 8, dan 28) sebagai anchor positif (bagian 8b butir 2). Langkah 19 memakai entri Paired pada langkah 17 sebagai anchor.
- Temuan untuk QA:
  - Pelaku approver (DD-41, DD-42) dan pelaku pair (DD-44, DD-45, DD-59) serta `Module` DD-44, DD-45, DD-59 hanya berupa placeholder (`[pelaku approver]`, `[pelaku user yang melakukan pair]`) di TC dan tidak ada di fixture Tabel Data Uji Dinamis; spec mengasersi judul tanpa nama pelaku atau `Module` bila nilainya tidak ditetapkan (Q-15).
  - TC-277 Expected a menulis `[pelaku admin yang Submit]` sedangkan Tabel Data Uji Dinamis menyebut Budi Santoso; spec memakai `Budi S`.
  - TC-280 Expected a menyebut `Module` berisi path menu modul asal pair "(format sama dengan hover Last Scanned In)" tanpa nilai tiap tag; spec memakai nilai `Fixed Asset > Register Asset` hanya untuk DD-43 (tersedia di fixture).
  - TC-369 langkah 1 menyebut DD-59 "dipasang ke aset lewat Pair TAG di FAMS tanpa Receive" tetapi fixture menyebut DD-59 berstatus `Paired` dengan riwayat lengkap; spec membaca riwayat fixture, tidak menjalankan Pair TAG di FAMS.
  - Isi `Asset` untuk `Paired` DD-59 dan `Reserved`/`Released` DD-42 tidak ditetapkan selain `Forklift 01`/`AST-0042`; spec memakai nilai itu hanya untuk DD-42.
  - Pembuatan fixture TAG Log (DD-39 sampai DD-59) antar spec tidak didefinisikan di TC (Q-4).
