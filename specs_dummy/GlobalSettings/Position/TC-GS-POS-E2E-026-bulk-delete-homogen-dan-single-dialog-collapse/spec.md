---
id: TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse
title: "Bulk Delete homogen bebas relasi berhasil, dialog collapse saat 1 item, scrollable list, dan guard double-click"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-137
  - TC-GS-POS-138
  - TC-GS-POS-139
  - TC-GS-POS-140
  - TC-GS-POS-141
  - TC-GS-POS-146
  - TC-GS-POS-150
coverage:
  web: automated
---

# Bulk Delete homogen bebas relasi berhasil, dialog collapse saat 1 item, scrollable list, dan guard double-click

## Prerequisites

- Login sebagai Total Control
- Record bulk homogen bebas relasi tersedia (misal 5 record dummy)

## Test Steps

### Collapse ke Dialog Single Saat 1 Item Terpilih

1. Centang tepat 1 baris Position bebas relasi
2. Klik tombol "[Delete]" pada Bulk Action Bar
3. Verifikasi dialog yang muncul adalah dialog konfirmasi single Delete Position (bukan dialog bulk)
4. Klik "[Cancel]", verifikasi seleksi dipertahankan

### Dialog Bulk Delete Homogen & Scrollable List

5. Centang 5 baris Position bebas relasi
6. Klik tombol "[Delete]" pada Bulk Action Bar
7. Verifikasi dialog konfirmasi "Delete Position" muncul menampilkan daftar nama seluruh item terpilih dalam bentuk list yang dapat di-scroll (tidak diringkas dengan kata "dan X lainnya")
8. Klik tombol "[Cancel]", verifikasi dialog tertutup dan kelima baris tetap terpilih

### Eksekusi Bulk Delete & Double-Click Guard

9. Klik kembali tombol "[Delete]" pada Bulk Action Bar
10. Klik tombol konfirmasi "[Delete]" pada dialog secara cepat dua kali
11. Verifikasi tombol masuk state loading dan permintaan hanya diproses satu kali
12. Verifikasi toast sukses "Success, position has been deleted." muncul dan seluruh record terpilih terhapus dari tabel

## Notes

- Menggabungkan TC-GS-POS-137, 138, 139, 140, 141, 146, dan 150.
