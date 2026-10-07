---
id: TC-GS-DIV-E2E-030-edit-modal-validasi-field-name-keunikan-dan-self-exclusion
title: "Validasi Keunikan Name pada Edit: Debounce Duplikat, Re-Cek Submit, Pengecualian Nilai Sendiri, dan Toleransi Case Rename"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-89
  - TC-GS-DIV-90
  - TC-GS-DIV-91
  - TC-GS-DIV-92
coverage:
  web: automated
---

# Validasi Keunikan Name pada Edit: Debounce Duplikat, Re-Cek Submit, Pengecualian Nilai Sendiri, dan Toleransi Case Rename

## Prerequisites

- Login sebagai Role: Total Control
- Division "Finance" sudah ada di entitas uji
- Buka Edit Division "Accounting"
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)
- Division `Finance` sudah ada

## Test Steps

### Edit Division Name menjadi duplikat Division lain menampilkan error (TC-GS-DIV-89)

1. Buka row action baris `Audit` lalu klik `Edit`
2. Ketik `finance` pada Division Name lalu berhenti mengetik ~500ms
3. Verifikasi Setelah debounce ~500ms muncul error inline `Division Name already exists`
4. Verifikasi Tombol `[Save]` tidak menyimpan perubahan ke nilai duplikat

### Save langsung dengan Division Name duplikat sebelum debounce selesai ditolak (TC-GS-DIV-90)

5. Buka row action baris `Audit` lalu klik `Edit`
6. Ketik `Finance` dan segera klik `[Save]` sebelum 500ms berlalu
7. Verifikasi Perubahan tidak tersimpan
8. Verifikasi Error inline `Division Name already exists` tampil dan modal tetap terbuka dengan input dipertahankan

### Mengetik ulang Division Name yang sama dengan nilai sendiri tidak menampilkan error duplicate (TC-GS-DIV-91)

9. Buka row action baris `Accounting` lalu klik `Edit`
10. Hapus lalu ketik ulang `Accounting` pada Division Name dan tunggu ~500ms
11. Verifikasi Tidak ada error duplicate terhadap diri sendiri pada Division Name

### Mengubah Division Name hanya pada huruf besar kecil tidak dianggap duplikat terhadap diri sendiri (TC-GS-DIV-92)

12. Buka row action baris `Accounting` lalu klik `Edit`
13. Ubah Division Name menjadi `ACCOUNTING` dan tunggu ~500ms
14. Verifikasi Tidak ada error `Division Name already exists` terhadap record itu sendiri

## Notes

- Memvalidasi aturan keunikan Name pada form Edit: error "Division Name already exists" setelah debounce ~500ms saat diubah menjadi nama divisi lain, re-cek atomik saat submit langsung sebelum debounce selesai, pengetikan ulang nama milik sendiri tidak memicu error duplicate (self-exclusion), dan perubahan hanya pada huruf besar-kecil pada record sendiri tidak dianggap duplikat (PRD §6, §9.4.2 baris Edit D5, V-04).
- Sumber pemetaan test case granular: TC-GS-DIV-89, TC-GS-DIV-90, TC-GS-DIV-91, TC-GS-DIV-92.
