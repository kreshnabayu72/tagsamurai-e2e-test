---
id: TC-GS-POS-E2E-048-race-edit-delete-record-sama
title: Race Edit dan Delete pada Record yang Sama
priority: High
caseType: Edge Case
status: draft
sourceTc:
  - TC-GS-POS-237
coverage:
  web: automated
---

# Race Edit dan Delete pada Record yang Sama

## Prerequisites

- Dua sesi browser bersamaan (`adminA`, `adminB`), login sebagai Role Total Control.
- Position bebas relasi: `P-Race-ED`.

## Test Steps

### A. Persiapan

1. Verifikasi `P-Race-ED` ada di tabel dan dapat diedit/dihapus.

### B. Skenario 1: Edit lalu Delete bersamaan (edit diproses dulu)

2. Di sesi `adminA`, buka form Edit `P-Race-ED`, ubah nama menjadi `P-Race-ED-Edited`, belum Submit.
3. Di sesi `adminB`, buka konfirmasi Delete `P-Race-ED` (dialog konfirmasi), belum klik Delete.
4. Submit Edit di `adminA` terlebih dahulu → sukses (atau sesuai).
5. Segera klik Delete di `adminB` → sistem harus menangani dengan benar (bisa gagal karena record tidak ditemukan/sudah berubah, atau ditangani via re-check).
6. Verifikasi state akhir konsisten: record mungkin sudah berubah nama, atau sudah terhapus; tidak ada inconsistent state.

### C. Skenario 2: Delete lalu Edit bersamaan

7. Kembalikan kondisi (buat ulang `P-Race-ED` jika terhapus di skenario 1).
8. Di sesi `adminA`, buka konfirmasi Delete `P-Race-ED`.
9. Di sesi `adminB`, buka form Edit `P-Race-ED`, ubah nama, belum Submit.
10. Klik Delete di `adminA` terlebih dahulu → sukses.
11. Submit Edit di `adminB` → Edit harus gagal (record not found / tidak bisa diedit karena sudah dihapus).
12. Verifikasi record benar-benar terhapus, tidak ada duplikasi, logging konsisten.

### D. Verifikasi akhir

13. Verifikasi tidak ada race yang menyebabkan data rusak (record hilang tanpa log, atau tetap ada dalam state tidak valid).
14. Verifikasi toast/error sesuai hasil masing-masing sesi.
15. Verifikasi logging di tiga surface sesuai operasi yang benar-benar berhasil.

## Notes

- Menguji re-check atomik saat Confirm (mirip race bulk namun single record). Operasi yang gagal karena race harus dilaporkan dengan jelas, bukan silent corruption.
