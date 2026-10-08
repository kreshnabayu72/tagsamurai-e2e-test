---
id: TC-GS-USER-E2E-032-validasi-scan-tag
title: Validasi Scan TAG untuk TAG yang tidak valid
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-60
  - TC-GS-USER-62
  - TC-GS-USER-61
  - TC-GS-USER-343
  - TC-GS-USER-344
  - TC-GS-USER-345
coverage:
  web: automated
---

# Validasi Scan TAG untuk TAG yang tidak valid

## Prerequisites

- Login sebagai Role: Total Control, entity Client pada plan Growth atau lebih tinggi (Scan TAG tampil)
- User "Sinta Dewi" tanpa TAG terpasang
- User "Rangga Saputra" sudah punya "TAG P" terpasang
- "TAG U": kode yang belum pernah diaktivasi dan tidak ada di registry entity ini
- "TAG O": terdaftar sebagai Object TAG, bukan User TAG
- "TAG P": sudah dipasang ke "Rangga Saputra"
- Setiap TAG hanya melanggar satu aturan, supaya pesan yang muncul menunjukkan aturan mana yang menolak
- Simulasi scan RFID: skrip bisa memasukkan kode TAG seolah hasil scan hardware. Kebutuhan ini disediakan tim FE
- Spec ini tidak menyimpan pairing apa pun, jadi tidak butuh cleanup

## Test Steps

### Dari User Detail

1. Buka User Detail "Sinta Dewi" dan klik `Scan TAG`
2. Scan "TAG U"
3. Verifikasi error "This TAG hasn't been activated yet. Please contact Admin." muncul dan badge tetap "Unverified"
4. Scan "TAG P"
5. Verifikasi error "Error, RFID TAG is already paired to another user." muncul dan badge tetap "Unverified"
6. Scan "TAG O"
7. Verifikasi error "Error, the scanned TAG is object TAG." muncul dan badge tetap "Unverified"

### Dari Modal Create

8. Klik `[+ User]` untuk membuka Modal Create
9. Klik `Scan TAG` lalu scan "TAG U"
10. Verifikasi toast "This TAG hasn't been activated yet. Please contact Admin." muncul, badge tetap "Unverified", dan form tidak terganggu
11. Scan "TAG P"
12. Verifikasi toast "Error, RFID TAG is already paired to another user." muncul dan badge tetap "Unverified"
13. Scan "TAG O"
14. Verifikasi toast "Error, the scanned TAG is object TAG." muncul dan badge tetap "Unverified"
15. Klik `✕` untuk menutup modal tanpa mengisi field lain

## Notes

- Spec ini dipisah dari alur pair biasa karena butuh TAG dengan kondisi khusus (prinsip 12 di `docs/e2e-conventions.md` bagian 3). Kebutuhan TAG-nya ditulis di Prerequisites untuk tim FE.
- Urutan validasi menurut PRD adalah belum diaktivasi, lalu sudah dipasang, lalu Object TAG. Karena tidak ada TC untuk TAG yang melanggar lebih dari satu aturan, urutan itu tidak diuji dengan kombinasi.
- Pair yang berhasil dicakup `TC-GS-USER-E2E-031-pair-unpair-tag`.
- Kegagalan pada Detail muncul sebagai pesan error, dan pada Modal Create sebagai toast, sesuai sumber TC.
