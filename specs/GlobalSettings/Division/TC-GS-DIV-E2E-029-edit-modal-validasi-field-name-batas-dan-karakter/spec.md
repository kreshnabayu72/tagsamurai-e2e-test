---
id: TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter
title: "Validasi Field Name pada Edit: Wajib Diisi, Spasi Saja, Trim Spasi, Batas 120/121 Karakter, dan Blokir Emoji"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-83
  - TC-GS-DIV-84
  - TC-GS-DIV-85
  - TC-GS-DIV-86
  - TC-GS-DIV-87
  - TC-GS-DIV-88
coverage:
  web: automated
---

# Validasi Field Name pada Edit: Wajib Diisi, Spasi Saja, Trim Spasi, Batas 120/121 Karakter, dan Blokir Emoji

## Prerequisites

- Login sebagai Role: Total Control
- Buka Edit Division
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)

## Test Steps

### Save Edit dengan Division Name dikosongkan (TC-GS-DIV-83)

1. Buka row action baris `Accounting` lalu klik `Edit`
2. Kosongkan Division Name
3. Klik `[Save]`
4. Verifikasi Pesan error inline `Division Name must not be empty` dengan border `severity="danger"`
5. Verifikasi Perubahan tidak tersimpan dan modal tetap terbuka

### Save Edit dengan Division Name hanya spasi (TC-GS-DIV-84)

6. Buka row action baris `Accounting` lalu klik `Edit`
7. Ganti Division Name dengan 3 spasi
8. Klik `[Save]`
9. Verifikasi Name diperlakukan kosong: pesan inline `Division Name must not be empty`
10. Verifikasi Perubahan tidak tersimpan

### Edit Division Name dengan spasi depan dan belakang disimpan ter-trim (TC-GS-DIV-85)

11. Buka row action baris `Administration` lalu klik `Edit`
12. Ubah Division Name menjadi `  General Administration  `
13. Klik `[Save]`
14. Lihat baris di tabel
15. Verifikasi Muncul toast sukses: `Success, division has been updated.`
16. Verifikasi Tabel menampilkan Name `General Administration` tanpa spasi di awal dan akhir

### Edit Division Name tepat 120 karakter berhasil disimpan (TC-GS-DIV-86)

17. Buka row action baris `Audit` lalu klik `Edit`
18. Ganti Division Name dengan 120 karakter
19. Klik `[Save]`
20. Verifikasi Tidak ada error pada Division Name
21. Verifikasi Muncul toast sukses: `Success, division has been updated.`
22. Verifikasi Tabel menampilkan Name baru utuh 120 karakter

### Edit Division Name 121 karakter diterima input dan menampilkan error inline (TC-GS-DIV-87)

23. Buka row action baris `Audit` lalu klik `Edit`
24. Ketik atau tempel 121 karakter pada Division Name
25. Verifikasi Input menerima seluruh 121 karakter
26. Verifikasi Langsung saat melebihi muncul error inline `Max. 120 characters`

### Edit Division Name berisi emoji menampilkan error inline (TC-GS-DIV-88)

27. Buka row action baris `Audit` lalu klik `Edit`
28. Ketik `Audit 😀` pada Division Name
29. Verifikasi Langsung saat mengetik muncul error inline `Division Name contains invalid characters`

## Notes

- Memvalidasi validasi format Name pada form Edit: error "Division Name must not be empty" saat dikosongkan atau diisi spasi saja, penyimpanan ter-trim, batas 120 karakter berhasil disimpan, error "Max. 120 characters" pada 121 karakter, dan error "Division Name contains invalid characters" pada emoji (PRD §6, §9.2, §9.9, V-01, V-02, V-03).
- Sumber pemetaan test case granular: TC-GS-DIV-83, TC-GS-DIV-84, TC-GS-DIV-85, TC-GS-DIV-86, TC-GS-DIV-87, TC-GS-DIV-88.
