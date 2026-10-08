---
id: TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter
title: "Validasi Field Name pada Create: Wajib Diisi, Spasi Saja, Batas 1 Karakter, Batas 120/121 Karakter, dan Emoji Terlarang"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-34
  - TC-GS-DIV-35
  - TC-GS-DIV-36
  - TC-GS-DIV-37
  - TC-GS-DIV-38
  - TC-GS-DIV-39
coverage:
  web: automated
---

# Validasi Field Name pada Create: Wajib Diisi, Spasi Saja, Batas 1 Karakter, Batas 120/121 Karakter, dan Emoji Terlarang

## Prerequisites

- Login sebagai Role: Total Control
- Buka Modal Create Division
- User berada di Global Settings > User > Division

## Test Steps

### Submit Create dengan Division Name kosong (TC-GS-DIV-34)

1. Klik `[+ Division]`
2. Biarkan Division Name kosong
3. Klik `[Submit]`
4. Verifikasi Border field Division Name berubah `severity="danger"`
5. Verifikasi Pesan error inline di bawah field: `Division Name must not be empty`
6. Verifikasi Record tidak dibuat dan modal tetap terbuka

### Submit Create dengan Division Name hanya berisi spasi (TC-GS-DIV-35)

7. Klik `[+ Division]`
8. Isi Division Name dengan 3 spasi
9. Klik `[Submit]`
10. Verifikasi Name diperlakukan kosong: pesan inline `Division Name must not be empty`
11. Verifikasi Record tidak dibuat dan modal tetap terbuka

### Division Name dengan spasi depan dan belakang disimpan ter-trim (TC-GS-DIV-36)

12. Klik `[+ Division]`
13. Isi Division Name `  Internal Affairs  `
14. Isi Code `IAF`
15. Klik `[Submit]`
16. Lihat baris di tabel
17. Verifikasi Muncul toast sukses: `Success, division has been created.`
18. Verifikasi Tabel menampilkan Name `Internal Affairs` tanpa spasi di awal dan akhir

### Division Name tepat 120 karakter berhasil disimpan (TC-GS-DIV-37)

19. Klik `[+ Division]`
20. Isi Division Name dengan 120 karakter
21. Isi Code `LONG120`
22. Klik `[Submit]`
23. Verifikasi Tidak ada pesan error pada field Division Name
24. Verifikasi Muncul toast sukses: `Success, division has been created.`
25. Verifikasi Baris tampil dengan Name utuh 120 karakter

### Division Name 121 karakter diterima input dan menampilkan error inline (TC-GS-DIV-38)

26. Klik `[+ Division]`
27. Ketik atau tempel 121 karakter pada Division Name
28. Perhatikan field dan pesan di bawahnya
29. Verifikasi Input menerima seluruh 121 karakter (tidak dipotong)
30. Verifikasi Langsung saat melebihi muncul error inline `Max. 120 characters` dengan border `severity="danger"`

### Division Name berisi emoji menampilkan error inline (TC-GS-DIV-39)

31. Klik `[+ Division]`
32. Ketik `Finance 😀` pada Division Name
33. Verifikasi Langsung saat mengetik muncul error inline `Division Name contains invalid characters`
34. Verifikasi Border field `severity="danger"`

## Notes

- Memvalidasi pesan error inline V-01 ("Division Name must not be empty"), V-02 ("Max. 120 characters" langsung saat melebihi), V-03 ("Division Name contains invalid characters" saat emoji), dan boundary 1 & 120 karakter (PRD §6, §9.9).
- Sumber pemetaan test case granular: TC-GS-DIV-34, TC-GS-DIV-35, TC-GS-DIV-36, TC-GS-DIV-37, TC-GS-DIV-38, TC-GS-DIV-39.
