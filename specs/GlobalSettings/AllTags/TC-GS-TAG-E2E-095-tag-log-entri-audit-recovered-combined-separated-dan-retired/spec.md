---
id: TC-GS-TAG-E2E-095-tag-log-entri-audit-recovered-combined-separated-dan-retired
title: "TAG Log: Entri Audit, Marked Damaged/Missing dan Recovered, Combined dan Separated, serta Retired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-283
  - TC-GS-TAG-284
  - TC-GS-TAG-285
  - TC-GS-TAG-286
coverage:
  web: automated
---

# TAG Log: Entri Audit, Marked Damaged/Missing dan Recovered, Combined dan Separated, serta Retired

## Prerequisites

- Mode: FE+BE.
- Akun aktor utama: Total Control Client Log Wulan Sari `totalControl_automated_qaLog@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_LOG_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Login sekali di hook `before` spec ini.
- Akun kedua (langkah 13 sampai 14, TC-283): Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`; kredensial `Spectra.env.GS_TC_AUDIT_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client Log (dibaca saja, tanpa aksi tulis; fixture TAG Log, Tabel Data Uji Dinamis TC, dibuat lewat fixture BE; mekanisme dan pelaku fixture disediakan tim FE/BE, lihat Temuan untuk QA):

| ID | Code | Riwayat yang diasersi |
|---|---|---|
| DD-49 | `E2801160600002054D8C0049` | `Activated`; `Retired` (Previous Status `Available`, dipensiunkan lewat FAMS atau Supply Asset) |
| DD-51 | `E2801160600002054D8C0051` | `Activated`; `Marked Damaged/Missing` (Previous Status `Available`, user FAMS); `Recovered` (Previous Status `Damaged/Missing`, user FAMS) |
| DD-52 | `E2801160600002054D8C0052` | `Activated`; `Combined` With NFC `04A224B2C15F53`; `Separated` From NFC `04A224B2C15F53` |

- Data Pre-setup Client Audit (precondition TC-283; dipulihkan ke kondisi awal oleh fixture BE sebelum langkah 15): Seed Client Audit AU1 `E2801160600002054D8A5001` (Available, combined dengan NFC `04A224B2C15E95` Available), AU2 `...5002` (Damaged/Missing), AU3 `...5003` (Retired), AU4 `...5004` (Available). Sesi Audit RFID selesai dibangun lewat fixture BE (jalur commit produk, tanpa pemindaian): AU1 sampai AU4 diaudit dengan AU2 terpindai (Verified), checkbox `Mark all as Damaged/Missing` dicentang saat Submit; dipakai sebagai precondition TC-283, hasilnya diasersi di TAG Log.
- Pelaku fixture (pelaku `Marked Damaged/Missing`, `Recovered`, `Combined`, `Separated`, `Retired`, dan pelaku Submit Audit) tidak disebut TC dan dibaca dari fixture (Q-15). Pelaku tampil sebagai `[First Name] [Last Initial]`.
- Kemampuan teknis: mengatur fixture TAG Log di atas pada Client Log dan Client Audit; mengganti akun (Logout lalu login) di tengah spec; Search registri agar baris target tampil.
- State global yang diubah: tidak ada selain data (Seed Client Audit dan log Client Audit).

## Test Steps

### TC-GS-TAG-284: Entri Marked Damaged/Missing dan Recovered dengan Previous Status

1. Ketik Search `E2801160600002054D8C0051`, tekan Enter, buka menu baris DD-51, klik `TAG Log`
2. Verifikasi entri `TAG Marked Damaged/Missing by` pelaku user memuat `Previous Status: Available`
3. Verifikasi entri `TAG Marked Damaged/Missing by` pelaku user tidak memuat baris `Note` (tidak dipicu `Receive Manually`)
4. Verifikasi entri `TAG Recovered by` pelaku user memuat `Previous Status: Damaged/Missing`
5. Tutup popup lewat `[✕]`

### TC-GS-TAG-285: Entri Combined dan Separated dengan tag pasangan

6. Ganti isi kotak search dengan `E2801160600002054D8C0052`, tekan Enter, buka menu baris DD-52, klik `TAG Log`
7. Verifikasi entri `TAG Combined by` pelaku admin memuat `Combined With: NFC 04A224B2C15F53`
8. Verifikasi entri `TAG Separated by` pelaku admin memuat `Separated From: NFC 04A224B2C15F53`
9. Tutup popup lewat `[✕]`

### TC-GS-TAG-286: Entri Retired dengan Previous Status

10. Ganti isi kotak search dengan `E2801160600002054D8C0049`, tekan Enter, buka menu baris DD-49, klik `TAG Log`
11. Verifikasi entri `TAG Retired by` pelaku user memuat `Previous Status: Available`
12. Tutup popup lewat `[✕]`

### TC-GS-TAG-283: Entri Audit, Result dan Status sebelum ke sesudah termasuk yang tidak berubah, tanpa baris Hardware

13. Klik avatar akun, pilih `Logout`
14. Login sebagai Total Control Client Audit Joko Santoso (`Spectra.env.GS_TC_AUDIT_PASSWORD`)
15. Pulihkan Seed Client Audit lewat fixture BE, lalu bangun sesi Audit RFID selesai dengan AU2 terpindai dan checkbox `Mark all as Damaged/Missing` dicentang
16. Buka Global Settings > TAG, klik Tab Not Paired, ketik Search `E2801160600002054D8A5002`, tekan Enter, buka menu baris AU2, klik `TAG Log`
17. Verifikasi entri `TAG Audited by` pelaku admin yang Submit memuat `Result: Verified` dan `Status: Damaged/Missing → Available`
18. Verifikasi TAG Log AU2 memuat tepat satu entri Audit untuk sesi itu
19. Verifikasi entri Audit AU2 tidak memuat baris `Hardware`
20. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `E2801160600002054D8A5004`, tekan Enter, buka menu baris AU4, klik `TAG Log`
21. Verifikasi entri `TAG Audited by` pelaku admin yang Submit memuat `Result: Not Found` dan `Status: Available → Damaged/Missing`
22. Verifikasi TAG Log AU4 memuat tepat satu entri Audit untuk sesi itu
23. Verifikasi entri Audit AU4 tidak memuat baris `Hardware`
24. Tutup popup lewat `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data (sesi Audit TC-283 dibangun sebagai precondition lewat fixture BE).
- Urutan TC dalam spec: 284, 285, 286, 283 (bukan urutan sumber). TC-283 memakai Client Audit sehingga ditaruh di akhir setelah ganti akun eksplisit (langkah 13 sampai 14); bagian itu tetap bermakna bila bagian sebelumnya gagal. Perubahan urutan dicatat sesuai S-05.
- Kelas: TC-283 berlabel `Manual Only — (b)` karena sesi Audit asal memakai pemindai; spec ini tidak memindai (sesi dibangun fixture BE dan hasilnya dibaca dari TAG Log), sehingga bukan kelas d. Pemindaian Audit diuji di spec 041 sampai 044.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 6, 10, 16, 20 (Search agar baris target tampil dan membuka TAG Log), langkah 5, 9, 12, 20, 24 (menutup popup), langkah 13 sampai 14 (ganti akun), langkah 15 (precondition TC-283).
- Langkah 3, 19, dan 23 (absence) memakai entri lain pada popup yang sama sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-283 menyatakan pelaku sebagai `[pelaku admin yang Submit]` dan tidak menyebut siapa yang men-Submit sesi precondition; spec membangun sesi lewat fixture BE (pelaku dibaca dari fixture, Q-15).
  - TC-283 langkah 1 hanya membuka TAG Log AU2 dan AU4; TAG Log AU1, AU3, dan sibling NFC tidak diasersi karena Expected tidak menyebutnya.
  - TC-283 Expected d ("satu entri Audit per baris sesi") diasersi sebagai satu entri Audit pada AU2 dan AU4 untuk sesi precondition.
  - Pelaku fixture TC-284, TC-285, TC-286 hanya berupa placeholder (`[pelaku user pelaku]`, `[pelaku admin pelaku]`, `[pelaku user FAMS atau Supply Asset]`); spec mengasersi judul tanpa nama pelaku (Q-15).
  - Pembuatan fixture TAG Log dan reset Seed Client Audit antar spec tidak didefinisikan di TC (Q-4).
