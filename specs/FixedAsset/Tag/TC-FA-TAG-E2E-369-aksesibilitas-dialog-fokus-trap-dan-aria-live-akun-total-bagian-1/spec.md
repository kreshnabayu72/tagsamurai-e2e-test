---
id: TC-FA-TAG-E2E-369-aksesibilitas-dialog-fokus-trap-dan-aria-live-akun-total-bagian-1
title: "Aksesibilitas: Focus Trap Dialog Replace, Pair, dan Print QR, Aria-Live Hasil Pindai, dan Label Ikon Tipe Tag"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-318
  - TC-FA-TAG-323
  - TC-FA-TAG-322
  - TC-FA-TAG-321
  - TC-FA-TAG-319
  - TC-FA-TAG-320
coverage:
  web: automated
---

# Aksesibilitas: Focus Trap Dialog Replace, Pair, dan Print QR, Aria-Live Hasil Pindai, dan Label Ikon Tipe Tag

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); pembacaan atribut aksesibilitas elemen (`aria-live`, label aksesibilitas) dan urutan fokus keyboard; seed idempotent aset dan stok Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired; AST-0051 'Excavator 20 Ton - 51' (Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet). Stok Global: Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available. Tag `RF-09999` tidak terdaftar (kode tidak dikenal).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan stok Tag dan kondisi reader ke keadaan awal lewat fixture backend. Spec ini tidak menekan [Submit] dan tidak mengubah state global. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-318: focus trap Dialog Replace TAG

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Tekan Tab berulang melewati seluruh elemen dialog
4. Verifikasi fokus hanya berpindah di antara elemen dalam dialog (checkbox, tombol Scan, [Cancel], [Submit], ikon close)
5. Tekan Shift+Tab dari elemen pertama
6. Verifikasi fokus tidak keluar ke tabel di belakang dialog

### TC-FA-TAG-323: label aksesibilitas ikon tipe Tag

7. Verifikasi ikon tipe Tag pada baris atas blok info memiliki label aksesibilitas `RFID · RF-00130`

### TC-FA-TAG-322: aria-live assertive pada pindaian gagal

8. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-09999`
9. Verifikasi pesan "Error, can't recognize TAG." pada slot diumumkan lewat atribut `aria-live="assertive"`

### TC-FA-TAG-321: aria-live polite pada pindaian sukses

10. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
11. Verifikasi area hasil ButtonScan memiliki atribut `aria-live="polite"`
12. Klik `✕` pada Dialog Replace TAG
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik [Leave]

### TC-FA-TAG-319: focus trap Dialog Pair TAG

15. Klik `Show` di samping `Not Paired Yet`
16. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
17. Tekan Tab berulang melewati seluruh elemen dialog
18. Verifikasi fokus hanya berpindah di antara elemen dalam dialog
19. Klik `✕` pada Dialog Pair TAG

### TC-FA-TAG-320: focus trap Dialog Print QR

20. Tutup Popup Detail
21. Klik tombol `Print QR`
22. Tekan Tab berulang melewati seluruh elemen dialog
23. Verifikasi fokus hanya berpindah di antara `Quantity`, pilihan `Start position`, [Cancel], [Start Print], dan ikon close

## Notes

- Spec aksesibilitas: teknologi bantu diamati lewat atribut `aria-live`, label aksesibilitas, dan urutan fokus keyboard; kelas fungsional.
- Urutan TC di dalam spec: 318, 323, 322, 321, 319, 320 (TC-FA-TAG-322 sebelum TC-FA-TAG-321 supaya pindaian gagal mendahului pindaian sukses pada slot yang sama dan dialog hanya dirty sekali; dialog Replace, Pair, dan Print QR dibuka berurutan).
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka Popup Detail dan dialog), 12 sampai 14 (menutup form dirty, S-08), 15 sampai 16 (membuka daftar Not Paired Yet dan Dialog Pair TAG), 19 (menutup dialog yang tidak dirty), 20 (menutup popup agar toolbar dapat diklik).
- Anchor positif: asersi fokus (langkah 4, 18, 23) memuat daftar elemen dialog yang sama-sama tampil; tidak ada asersi absence yang berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-TAG-318 mencantumkan "checkbox" sebagai elemen dialog tanpa menyebut checkbox apa; spec mengikuti teks TC.
  - TC-FA-TAG-321 dan TC-FA-TAG-322 tidak menyebut perilaku slot setelah pindaian sukses berikutnya pada slot yang sama; spec memindai RF-00412 sesudah RF-09999 pada slot `RFID TAG`.
  - TC-FA-TAG-319 dan TC-FA-TAG-320 tidak menyebut apakah fokus kembali ke elemen pertama; spec mengasersi sesuai Expected TC saja.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
