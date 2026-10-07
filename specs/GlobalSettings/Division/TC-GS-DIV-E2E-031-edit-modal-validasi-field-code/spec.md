---
id: TC-GS-DIV-E2E-031-edit-modal-validasi-field-code
title: "Validasi Code pada Edit: Auto-Uppercase, Batas 15 Karakter, Karakter Terlarang, Duplikat, dan Pengecualian Nilai Sendiri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-93
  - TC-GS-DIV-94
  - TC-GS-DIV-95
  - TC-GS-DIV-96
  - TC-GS-DIV-97
coverage:
  web: automated
---

# Validasi Code pada Edit: Auto-Uppercase, Batas 15 Karakter, Karakter Terlarang, Duplikat, dan Pengecualian Nilai Sendiri

## Prerequisites

- Login sebagai Role: Total Control
- Buka Edit Division "Treasury"
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)
- Division `Finance` dengan Code `FIN` sudah ada

## Test Steps

### Edit Code dengan huruf kecil disimpan uppercase dan ter-trim (TC-GS-DIV-93)

1. Buka row action baris `Administration` lalu klik `Edit`
2. Ubah Code menjadi ` adm-9 `
3. Klik `[Save]`
4. Verifikasi Saat mengetik Code berubah menjadi huruf besar otomatis
5. Verifikasi Muncul toast sukses: `Success, division has been updated.`
6. Verifikasi Tabel menampilkan Code `ADM-9` tanpa spasi

### Edit Code 16 karakter diterima input dan menampilkan error inline (TC-GS-DIV-94)

7. Buka row action baris `Audit` lalu klik `Edit`
8. Ketik 16 karakter pada Code
9. Verifikasi Input menerima seluruh 16 karakter
10. Verifikasi Langsung saat melebihi muncul error inline `Max. 15 characters`

### Edit Code dengan karakter di luar whitelist menampilkan error inline (TC-GS-DIV-95)

11. Buka row action baris `Audit` lalu klik `Edit`
12. Ketik `AUD#1` pada Code
13. Verifikasi Langsung saat mengetik muncul error inline `Code contains invalid characters`

### Edit Code menjadi duplikat Division lain menampilkan error (TC-GS-DIV-96)

14. Buka row action baris `Audit` lalu klik `Edit`
15. Ketik `fin` pada Code lalu berhenti mengetik ~500ms
16. Verifikasi Code berubah menjadi `FIN`
17. Verifikasi Setelah debounce ~500ms muncul error inline `Code already exists`

### Mengetik ulang Code milik sendiri tidak menampilkan error duplicate (TC-GS-DIV-97)

18. Buka row action baris `Accounting` lalu klik `Edit`
19. Hapus lalu ketik ulang `acc` pada Code dan tunggu ~500ms
20. Verifikasi Code berubah menjadi `ACC`
21. Verifikasi Tidak ada error `Code already exists` terhadap record itu sendiri

## Notes

- Memvalidasi auto-uppercase, panjang maks 15 char, whitelist karakter, dan cek duplikat code record lain vs nilai sendiri (PRD §6, §9.9).
- Sumber pemetaan test case granular: TC-GS-DIV-93, TC-GS-DIV-94, TC-GS-DIV-95, TC-GS-DIV-96, TC-GS-DIV-97.
