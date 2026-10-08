---
id: TC-GS-DIV-E2E-028-edit-modal-screening-prefill-dan-aksesibilitas
title: "Screening Modal Edit Division: Pre-fill Nilai Name dan Code, Ketiadaan Checkbox Stay, Autofocus, dan Aksesibilitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-81
  - TC-GS-DIV-82
  - TC-GS-DIV-113
  - TC-GS-DIV-291
coverage:
  web: automated
---

# Screening Modal Edit Division: Pre-fill Nilai Name dan Code, Ketiadaan Checkbox Stay, Autofocus, dan Aksesibilitas

## Prerequisites

- Login sebagai Role: Total Control
- Division "Treasury" (Code "TRS") ada di entitas
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)
- Division `Training` (Code `TRN`) ada

## Test Steps

### Screening Popup Edit Division (TC-GS-DIV-81)

1. Buka row action baris `Accounting` lalu klik `Edit`
2. Verifikasi Title `Edit Division`
3. Verifikasi Icon close `[✕]`
4. Verifikasi Field `Division Name *` terisi `Accounting`
5. Verifikasi Field `Code` terisi `ACC` dengan helper text `Letters, numbers, hyphens, underscores, and dots only`
6. Verifikasi Checkbox `Stay on this form after submitting` tidak tampil (khusus mode Create)
7. Verifikasi Tombol `[Clear Field]` dan `[Save]` rata kanan; tidak ada tombol `[Cancel]`

### Tombol Save masuk Saving state dan seluruh kontrol form disabled (TC-GS-DIV-82)

8. Buka row action baris `Accounting` lalu klik `Edit`
9. Tahan (delay) respons simpan di network
10. Ubah Division Name menjadi `Accounting Team`
11. Klik `[Save]`
12. Verifikasi Tombol `[Save]` menampilkan spinner dan disabled
13. Verifikasi Seluruh kontrol form dan icon `[✕]` ikut disabled hingga proses simpan selesai

### Edit Division yang sudah dihapus pihak lain menampilkan toast tidak tersedia (TC-GS-DIV-113)

14. Admin A membuka Edit Division `Training`
15. Admin B menghapus Division `Training`
16. Admin A mengubah Name menjadi `Training Center` dan klik `[Save]`
17. Verifikasi Muncul toast netral: `This division is no longer available.`
18. Verifikasi Daftar Division di-refresh dan baris `Training` tidak ada
19. Verifikasi Perubahan tidak tersimpan

### Accessibility Popup Edit Division: fokus awal, aria, focus trap, Esc (TC-GS-DIV-291)

20. Buka row action baris `Accounting` lalu klik `Edit`
21. Perhatikan elemen yang mendapat fokus
22. Kosongkan Name lalu klik `[Save]` dan periksa atribut field Name
23. Isi kembali Name `Accounting`, lalu tekan Tab berulang melewati seluruh elemen
24. Tekan Esc
25. Verifikasi Kursor otomatis fokus pada input Division Name saat modal Edit terbuka
26. Verifikasi Field Division Name memiliki `aria-required="true"` dan error field terhubung lewat `aria-describedby`
27. Verifikasi Fokus keyboard tidak keluar dari modal (focus trap)
28. Verifikasi Esc menutup modal tanpa dialog karena nilai form sama dengan nilai tersimpan

## Notes

- Memvalidasi form Edit Division: title "Edit Division", prefill data Name dan Code, ketiadaan checkbox Stay, footer [Clear Field] dan [Save], autofocus, dan focus trap (PRD §4.2c, §4.5).
- Sumber pemetaan test case granular: TC-GS-DIV-81, TC-GS-DIV-82, TC-GS-DIV-113, TC-GS-DIV-291.
