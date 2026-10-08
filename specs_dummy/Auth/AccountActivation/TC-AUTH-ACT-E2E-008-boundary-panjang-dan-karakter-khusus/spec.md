---
id: TC-AUTH-ACT-E2E-008-boundary-panjang-dan-karakter-khusus
title: "Boundary panjang password 72 karakter dan karakter khusus pada checklist"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-30
  - TC-AUTH-ACT-31
  - TC-AUTH-ACT-32
  - TC-AUTH-ACT-33
  - TC-AUTH-ACT-34
  - TC-AUTH-ACT-35
  - TC-AUTH-ACT-36
coverage:
  web: automated
---

# Boundary panjang password 72 karakter dan karakter khusus pada checklist

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run).
- Akses API read-only untuk memastikan token tetap Active (spec ini tidak pernah men-submit form).
- Kemampuan paste teks panjang ke field Password (nilai 80 karakter disiapkan oleh skrip, bukan diketik manual).

## Test Steps

### Simbol ASCII non-alfanumerik dihitung karakter spesial (TC-AUTH-ACT-30)

1. Buka link aktivasi user seeding → halaman Set Password tampil.
2. Ketik `Abcdefg1_` pada field Password.
3. Verifikasi baris "One special character" hitam (primary) + ✓ untuk karakter `_`.
4. Kosongkan field, lalu ketik `Abcdefg1#`.
5. Verifikasi baris "One special character" hitam + ✓ untuk karakter `#`.
6. Kosongkan field, lalu ketik `Abcdefg1-`.
7. Verifikasi baris "One special character" hitam + ✓ untuk karakter `-`.
8. Kosongkan field, lalu ketik `Abcdefg1~`.
9. Verifikasi baris "One special character" hitam + ✓ untuk karakter `~`.

### Huruf berdiakritik dan emoji diterima tetapi bukan karakter spesial (TC-AUTH-ACT-31)

10. Kosongkan field Password, lalu ketik `Abcdefg1é`.
11. Verifikasi karakter `é` masuk ke field (tidak diblokir) dan baris "One special character" tetap abu-abu (disabled) + ○.
12. Kosongkan field Password, lalu ketik `Abcdefg1😀`.
13. Verifikasi karakter `😀` masuk ke field (tidak diblokir) dan baris "One special character" tetap abu-abu + ○.

### Error "Max. 72 characters" real-time pada field Password (TC-AUTH-ACT-32, TC-AUTH-ACT-33)

14. Kosongkan field Password, lalu ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter).
15. Verifikasi pesan "Max. 72 characters" tidak muncul dan seluruh baris checklist hitam + ✓.
16. Ketik satu karakter `x` tambahan sehingga total 73 karakter.
17. Verifikasi pesan inline "Max. 72 characters" muncul di bawah field Password seketika tanpa menekan button "Set Password".
18. Verifikasi Password Policy checklist tetap aktif dan tetap memperbarui status barisnya.

### Paste 80 karakter tersimpan penuh di field (TC-AUTH-ACT-34)

19. Kosongkan field Password, lalu paste teks 80 karakter (`Aa1!` diikuti 76 karakter `x`).
20. Verifikasi pesan "Max. 72 characters" muncul real-time.
21. Klik ikon toggle di field Password untuk melihat isi field.
22. Verifikasi field Password berisi seluruh 80 karakter yang di-paste (tidak dipotong menjadi 72).
23. Klik ikon toggle kembali untuk mengembalikan field ke keadaan masked.

### Pesan hilang real-time saat panjang kembali 72 (TC-AUTH-ACT-35)

24. Kembalikan isi field Password menjadi `Aa1!` diikuti 69 karakter `x` (total 73 karakter).
25. Verifikasi pesan "Max. 72 characters" tampil.
26. Hapus satu karakter sehingga total 72 karakter.
27. Verifikasi pesan "Max. 72 characters" hilang seketika tanpa menekan button "Set Password".
28. Ketik satu karakter `x` lagi sehingga total 73 karakter.
29. Verifikasi pesan "Max. 72 characters" muncul kembali seketika.

### Boundary pada field Confirm Password (TC-AUTH-ACT-36)

30. Setel field Password menjadi tepat 72 karakter (`Aa1!` diikuti 68 karakter `x`).
31. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) pada field Confirm Password.
32. Verifikasi tidak ada pesan "Max. 72 characters" pada field Confirm Password.
33. Ketik satu karakter `x` tambahan di field Confirm Password sehingga total 73 karakter.
34. Verifikasi pesan inline "Max. 72 characters" muncul di bawah field Confirm Password seketika.
35. Verifikasi tidak ada pesan "Max. 72 characters" pada field Password.

## Notes

- Seluruh kasus hanya mengetik/menempel pada field tanpa submit, sehingga satu user seeding cukup dan token tetap Active.
- Nilai batas (72, 73, 80 karakter) ditempel ke sesi yang sama karena assert tidak saling bentrok; setiap field diperiksa pada langkahnya sendiri agar penyebab kegagalan jelas.
- Kebutuhan paste teks panjang dicatat di Prerequisites.
