---
id: TC-FA-TAG-E2E-370-aksesibilitas-dialog-fokus-trap-dan-aria-live-akun-total-bagian-2
title: "Aksesibilitas: Focus Trap Dialog Receive TAG, Receive Manually, dan Decline Report serta Aria-Live Hasil Scan Receive TAG"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-571
  - TC-FA-TAG-572
  - TC-FA-TAG-570
  - TC-FA-TAG-597
  - TC-FA-TAG-1447
coverage:
  web: automated
---

# Aksesibilitas: Focus Trap Dialog Receive TAG, Receive Manually, dan Decline Report serta Aria-Live Hasil Scan Receive TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); pembacaan atribut aksesibilitas elemen (`aria-live`) dan urutan fokus keyboard; seed idempotent Tag To Be Returned, aset, dan laporan Tag lewat fixture backend.
- Data Pre-setup Tag To Be Returned (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.). Tag RF-00500 berstatus Available di Global (tidak ada di To Be Returned). Aset AST-0020 'Excavator 20 Ton - 20' (Group Plant B) dengan Tag tunggal RF-00130 punya laporan terbuka Damaged dari Staff Auditor.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned, laporan Tag, dan kondisi reader ke keadaan awal lewat fixture backend. Spec ini tidak menekan [Receive], [Submit], atau konfirmasi aksi, jadi data tidak berubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-571, TC-FA-TAG-572, dan TC-FA-TAG-570: Dialog Receive TAG

1. Buka Fixed Asset > TAG > To Be Returned
2. Klik tombol "Receive TAG"
3. Pindai Tag RF-00500
4. Verifikasi pesan error inline "This TAG is not in the To Be Returned list." berada pada region dengan atribut aria-live="assertive"
5. Pindai Tag RF-00071
6. Verifikasi hasil scan sukses (penambahan RF-00071 ke daftar sesi) diumumkan pada region dengan atribut aria-live="polite"
7. Tekan Tab berulang kali melewati seluruh elemen dialog
8. Tekan Shift+Tab dari elemen pertama
9. Verifikasi fokus berpindah hanya di antara elemen dalam dialog (ButtonScan, [Cancel], [Receive]) dan kembali ke elemen pertama tanpa keluar ke halaman di belakang
10. Klik `✕` pada Dialog Receive TAG
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik [Leave]

### TC-FA-TAG-597: Dialog Receive Manually

13. Buka menu aksi baris RF-00071
14. Klik "Receive Manually"
15. Tekan Tab berulang kali melewati seluruh elemen dialog
16. Verifikasi fokus berputar hanya di antara Textarea "Note", [Cancel], dan [Submit] serta kontrol penutup dialog tanpa keluar ke halaman di belakang
17. Klik `✕` pada Dialog Receive Manually

### TC-FA-TAG-1447: Dialog Decline Report

18. Buka tab Paired
19. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
20. Buka menu aksi baris Excavator 20 Ton - 20
21. Klik "Decline Report"
22. Tekan Tab berulang kali melewati seluruh elemen dialog
23. Verifikasi fokus berputar hanya di antara Textarea "Reason", [Cancel], dan [Submit] serta kontrol penutup dialog
24. Verifikasi fokus tidak keluar ke halaman di belakang dialog

## Notes

- Spec aksesibilitas: teknologi bantu diamati lewat atribut `aria-live` dan urutan fokus keyboard; kelas fungsional.
- Urutan TC di dalam spec: 571, 572, 570, 597, 1447 (TC-FA-TAG-571 sebelum TC-FA-TAG-572 supaya pindaian gagal mendahului pindaian sukses; TC-FA-TAG-570 memakai dialog yang sudah berisi RF-00071 karena langkah 3 TC itu memindai RF-00071 agar [Receive] aktif).
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka tab dan dialog), 10 sampai 12 (menutup form dirty, S-08), 13 dan 14 (membuka Dialog Receive Manually), 17 (menutup dialog yang tidak dirty), 18 sampai 21 (membuka Dialog Decline Report).
- Anchor positif: asersi fokus memuat daftar elemen dialog yang tampil; tidak ada asersi absence yang berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-TAG-570 mencantumkan elemen dialog "ButtonScan, [Cancel], [Receive]" sementara TC-FA-TAG-597 dan TC-FA-TAG-1447 menyebut "kontrol penutup dialog"; spec mengikuti teks TC.
  - TC-FA-TAG-571 tidak menyebut cara mengosongkan hasil sebelumnya sebelum pindaian RF-00071; spec memindai RF-00071 pada dialog yang sama.
  - TC-FA-TAG-597 dan TC-FA-TAG-1447 tidak menyebut Post Condition; tidak ada yang diasersi di luar Expected.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
