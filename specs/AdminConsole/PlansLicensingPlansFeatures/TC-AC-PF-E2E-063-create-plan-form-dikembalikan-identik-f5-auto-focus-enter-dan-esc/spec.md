---
id: TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc
title: "Create Plan: Form Identik, F5, Auto-Focus, Enter, dan Esc"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-160
  - TC-AC-PF-161
  - TC-AC-PF-704
  - TC-AC-PF-731
  - TC-AC-PF-736
  - TC-AC-PF-741
coverage:
  web: automated
---

# Create Plan: Form Identik, F5, Auto-Focus, Enter, dan Esc

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth`.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name `Paket Enter-{runId}-063` dan `Paket Dirty-{runId}-063` (bersuffix `-{runId}-063`); tidak ada plan yang tersimpan.
- Kemampuan teknis tambahan: dialog `beforeunload` bawaan browser pada F5 dapat dikonfirmasi atau dibatalkan oleh spec; tombol Esc dan klik area gelap di luar dialog dapat dijalankan spec.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir pada halaman Default > Active tanpa form dirty; hook `after` memulihkan Dataset.

## Test Steps

### Auto-focus dan Enter (TC-AC-PF-731)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Verifikasi saat form muncul fokus langsung berada di field Product
4. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Enter-{runId}-063`
5. Tekan Enter saat fokus berada di field Plan Name
6. Verifikasi Enter tidak men-submit: tidak ada toast
7. Verifikasi form tetap terbuka dengan input dipertahankan dan tidak ada perubahan data

### Esc pada form dirty (TC-AC-PF-736)

8. Tekan Esc
9. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Klik `[Cancel]` pada dialog
11. Verifikasi user tetap di form dengan input dipertahankan

### F5 pada form dirty (TC-AC-PF-161)

12. Tekan F5
13. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul karena form dirty
14. Batalkan konfirmasi `beforeunload` sehingga user tetap di form

### Form dikembalikan identik (TC-AC-PF-160)

15. Klik `[Clear Field]` agar form kembali ke kondisi awal
16. Pilih Product `FAMS`
17. Ketik `a` pada Plan Name lalu hapus kembali sehingga kosong
18. Klik segmen `Plans & Features` pada breadcrumb
19. Verifikasi form dianggap clean: halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung tanpa dialog Unsaved Changes

### Esc pada form bersih (TC-AC-PF-741)

20. Buka tab `Custom`, sub-tab `Active`
21. Klik `+ Custom Plan` pada toolbar
22. Tekan Esc tanpa mengubah apa pun
23. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung tanpa dialog Unsaved Changes

### Dialog Unsaved Changes pada Default Plan (TC-AC-PF-704)

24. Klik `+ Default Plan`
25. Pilih Product `SAMS` dan isi Plan Name `Paket Dirty-{runId}-063`
26. Klik segmen `Plans & Features` pada breadcrumb
27. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
28. Klik area gelap di luar dialog
29. Verifikasi klik area di luar dialog tidak menutup dialog
30. Tekan Esc
31. Verifikasi Esc menutup dialog seperti `[Cancel]`: user tetap di form New Default Plan dengan input dipertahankan
32. Klik segmen `Plans & Features` pada breadcrumb, klik `[Leave]` pada dialog `Unsaved Changes`

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 14, 15, 20, 32.
- Form TC-AC-PF-731 dilanjutkan oleh TC-AC-PF-736 dan TC-AC-PF-161: Product, Template, dan Plan Name sudah terisi sehingga langkah "Klik `+ Custom Plan`" dan pengisian TC-AC-PF-736 tidak diulang. Langkah `[Clear Field]` sebelum TC-AC-PF-160 mengembalikan form ke kondisi pristine agar TC itu mulai dari form tanpa isi.
- Langkah penghubung: membatalkan konfirmasi `beforeunload` sesudah F5, `[Clear Field]`, serta penutupan form dirty terakhir lewat breadcrumb dan `[Leave]` (S-08).
- Temuan untuk QA: (1) TC-AC-PF-741 mulai dari Custom > Active dan Expected kembali ke Default > Active, konsisten dengan TC-AC-PF-156 dan TC-AC-PF-159 tetapi tidak dijelaskan di TC.
