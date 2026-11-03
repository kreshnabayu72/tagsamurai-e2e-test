---
id: TC-FA-TAG-E2E-371-aksesibilitas-aria-live-buttonscan-dan-focus-trap-dialog-report-dan
title: "Aksesibilitas: Aria-Live Hasil ButtonScan Overlay Scan Replace dan Focus Trap Dialog Report TAG dan Cancel Report TAG"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-24
  - TC-FA-TAG-635
  - TC-FA-TAG-1448
coverage:
  web: automated
---

# Aksesibilitas: Aria-Live Hasil ButtonScan Overlay Scan Replace dan Focus Trap Dialog Report TAG dan Cancel Report TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Manage asset & TAG (Read + Update) `manageAssetTagReadUpdate_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode MU), password `Spectra.env.FA_TAG_MU_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
  - Staff Auditor (tidak memegang Manage asset & TAG) `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode SA_NOTAG), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD`. Dipakai pada langkah ganti akun (langkah 7 dan 8).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); pembacaan atribut aksesibilitas elemen (`aria-live`) dan urutan fokus keyboard; seed idempotent aset, Tag, task Existence Audit, dan laporan Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): aset AST-0221 'Excavator 20 Ton - 221' (Group Plant A) punya Tag RFID `RF-00140` berstatus Paired (Tag yang dipindai pada langkah 4); Tag `RF-09999` tidak terdaftar (kode tidak dikenal). Task Existence Audit dengan item AST-0044 'Excavator 20 Ton - 44' (group Plant B) berstatus In Audit; Tag [RFID] RF-00132 dan [QR] QR-00232 keduanya Paired tanpa laporan terbuka. Item AST-0020 'Excavator 20 Ton - 20' pada task yang sama dengan Tag tunggal RF-00130 yang punya laporan terbuka Damaged dari Staff Auditor.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader, task Existence Audit, dan laporan Tag ke keadaan awal lewat fixture backend, lalu kembalikan sesi ke akun default suite. Spec ini tidak menekan [Submit] atau [Cancel Report], jadi data tidak berubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-24: aria-live hasil ButtonScan

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-09999` (pemindaian gagal)
3. Verifikasi pesan galat diumumkan dengan `aria-live="assertive"`
4. Pindai Tag `RF-00140` (pemindaian sukses)
5. Verifikasi pesan sukses diumumkan dengan `aria-live="polite"`
6. Tutup overlay scan atau dialog yang terbuka lewat `✕`

### Ganti akun

7. Logout dari akun Manage asset & TAG (Read + Update)
8. Login sebagai Staff Auditor (tidak memegang Manage asset & TAG) (SA_NOTAG)

### TC-FA-TAG-635: focus trap Dialog Report TAG

9. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
10. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
11. Tekan Tab berulang kali melewati seluruh elemen dialog
12. Verifikasi fokus berputar hanya di antara checkbox Tag, Radio "Report Type", Textarea "Note", [Cancel], dan [Submit] serta kontrol penutup dialog tanpa keluar ke halaman di belakang
13. Klik `✕` pada Dialog Report TAG

### TC-FA-TAG-1448: focus trap Dialog Cancel Report TAG

14. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
15. Tekan Tab berulang kali melewati seluruh elemen dialog
16. Verifikasi fokus berputar hanya di antara Textarea "Reason", [Keep Report], dan [Cancel Report] serta kontrol penutup dialog
17. Verifikasi fokus tidak keluar ke halaman di belakang dialog

## Notes

- Spec aksesibilitas: teknologi bantu diamati lewat atribut `aria-live` dan urutan fokus keyboard; kelas fungsional.
- Urutan di dalam spec: pindaian gagal (langkah 2) sebelum pindaian sukses (langkah 4) agar overlay scan yang sama masih terbuka saat pesan galat diperiksa; urutan di TC-FA-TAG-24 terbalik (sukses lebih dulu).
- Langkah penghubung (tanpa awalan `Verifikasi`): 6 (menutup overlay atau dialog), 7 dan 8 (ganti akun), 9 (navigasi), 13 (menutup dialog yang tidak dirty).
- Anchor positif: asersi fokus memuat daftar elemen dialog yang sama-sama tampil; tidak ada asersi absence yang berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-TAG-24 berlabel Manual Only (interaksi hardware reader); spec tetap ditulis dengan simulator reader sebagai kemampuan yang disediakan tim FE/BE.
  - TC-FA-TAG-24 tidak menyebut Tag yang dipindai pada pemindaian sukses dan gagal serta hasil setelah pemindaian sukses di overlay scan; spec memakai `RF-00140` (sukses) dan `RF-09999` (gagal) dan menutup lewat langkah 6.
  - TC-FA-TAG-24 menyebut precondition "Reader terhubung" dengan Role Manage asset & TAG (Read + Update); TC-FA-TAG-635 dan TC-FA-TAG-1448 memakai Role Staff Auditor (tidak memegang Manage asset & TAG) tanpa menyebut tab In Audit untuk TC-FA-TAG-1448; spec memakai tab yang sama dengan TC-FA-TAG-635.
  - Nilai literal Pre-setup (ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
