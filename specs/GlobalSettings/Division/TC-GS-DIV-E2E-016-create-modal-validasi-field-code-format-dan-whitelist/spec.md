---
id: TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist
title: "Validasi Field Code pada Create: Auto-Uppercase, Batas 15/16 Karakter, Simbol Terlarang, Whitelist (-_.), dan Spasi Saja"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-43
  - TC-GS-DIV-44
  - TC-GS-DIV-45
  - TC-GS-DIV-46
  - TC-GS-DIV-47
  - TC-GS-DIV-49
coverage:
  web: automated
---

# Validasi Field Code pada Create: Auto-Uppercase, Batas 15/16 Karakter, Simbol Terlarang, Whitelist (-_.), dan Spasi Saja

## Prerequisites

- Login sebagai Role: Total Control
- Buka Modal Create Division
- User berada di Global Settings > User > Division

## Test Steps

### Create dengan Code manual huruf kecil disimpan uppercase dan ter-trim (TC-GS-DIV-43)

1. Klik `[+ Division]`
2. Isi Division Name `Legal Affairs`
3. Isi Code ` la-01 `
4. Klik `[Submit]`
5. Verifikasi Saat mengetik Code berubah menjadi huruf besar otomatis
6. Verifikasi Muncul toast sukses: `Success, division has been created.`
7. Verifikasi Tabel menampilkan Code `LA-01` tanpa spasi

### Code tepat 15 karakter berhasil disimpan (TC-GS-DIV-44)

8. Klik `[+ Division]`
9. Isi Division Name `Network Operations`
10. Isi Code 15 karakter
11. Klik `[Submit]`
12. Verifikasi Tidak ada pesan error pada field Code
13. Verifikasi Muncul toast sukses: `Success, division has been created.`
14. Verifikasi Tabel menampilkan Code `CODE-15-CHARS-A`

### Code 16 karakter diterima input dan menampilkan error inline (TC-GS-DIV-45)

15. Klik `[+ Division]`
16. Ketik 16 karakter pada Code
17. Verifikasi Input menerima seluruh 16 karakter
18. Verifikasi Langsung saat melebihi muncul error inline `Max. 15 characters`

### Code dengan karakter di luar whitelist menampilkan error inline (TC-GS-DIV-46)

19. Klik `[+ Division]`
20. Ketik `FIN@1` pada Code
21. Verifikasi Langsung saat mengetik muncul error inline `Code contains invalid characters`

### Code dengan huruf, angka, hyphen, underscore, dan titik diterima (TC-GS-DIV-47)

22. Klik `[+ Division]`
23. Isi Division Name `Plant Maintenance`
24. Isi Code `pm-1_a.b`
25. Klik `[Submit]`
26. Verifikasi Tidak ada error pada Code
27. Verifikasi Muncul toast sukses: `Success, division has been created.`
28. Verifikasi Tabel menampilkan Code `PM-1_A.B`

### Code berisi spasi saja dianggap kosong dan di-generate otomatis (TC-GS-DIV-49)

29. Klik `[+ Division]`
30. Isi Division Name `Quality Control`
31. Isi Code dengan 3 spasi
32. Klik `[Submit]`
33. Verifikasi Tidak ada error pada Code
34. Verifikasi Muncul toast sukses: `Success, division has been created.`
35. Verifikasi Tabel menampilkan Code `QC` hasil auto-generate

## Notes

- Memvalidasi auto-uppercase (FI-02), V-05 ("Max. 15 characters"), V-06 ("Code contains invalid characters"), dukungan simbol `-_.`, dan penanganan spasi saja memicu auto-generate (PRD §4.4, §6, §9.9).
- Sumber pemetaan test case granular: TC-GS-DIV-43, TC-GS-DIV-44, TC-GS-DIV-45, TC-GS-DIV-46, TC-GS-DIV-47, TC-GS-DIV-49.
