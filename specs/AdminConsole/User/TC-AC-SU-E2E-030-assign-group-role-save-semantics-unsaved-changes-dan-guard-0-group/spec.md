---
id: TC-AC-SU-E2E-030-assign-group-role-save-semantics-unsaved-changes-dan-guard-0-group
title: "Assign Group Role: toggle ON kosong, Save replace PUT, toast assigned/updated, no-op, guard 0 group, dan dialog Unsaved Changes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-78
  - TC-AC-SU-79
  - TC-AC-SU-96
  - TC-AC-SU-99
  - TC-AC-SU-101
  - TC-AC-SU-250
  - TC-AC-SU-251
  - TC-AC-SU-257
  - TC-AC-SU-259
coverage:
  web: automated
---

# Assign Group Role: toggle ON kosong, Save replace PUT, toast assigned/updated, no-op, guard 0 group, dan dialog Unsaved Changes

## Prerequisites

- Login sebagai Role: Principal Total Control
- Target pengguna memiliki Group Role yang belum pernah di-assign

## Test Steps

### Toggle ON Role Kosong dan Revert saat Dibatalkan

1. Klik switch toggle ON pada Group Role yang belum pernah di-assign
2. Verifikasi popup Assign Group Role otomatis terbuka secara wajib
3. Klik icon `[✕]` di header popup atau tekan `Esc`
4. Verifikasi popup tertutup dan switch toggle otomatis revert kembali ke posisi OFF tanpa menyimpan perubahan

### Save Semantics (PUT Replace), Toast Sukses, dan No-Op

1. Klik switch toggle ON kembali, tambahkan 1 group baru via `[+ Assign Group]` lalu klik `[Save]`
2. Verifikasi popup tertutup dan muncul toast: `"Success, group role has been assigned."` / `"Success, group role has been updated."`
3. Buka kembali popup, hapus 1 group dari daftar dan klik `[Save]`
4. Verifikasi PUT replace semantics berjalan (penugasan akhir persis sesuai payload baru)
5. Buka kembali popup tanpa melakukan perubahan apa pun lalu klik `[Save]`
6. Verifikasi popup tertutup dengan toast netral: `"No changes to save."` (tanpa log perubahan)

### Guard 0 Group dan Dialog Unsaved Changes

1. Buka popup Assign Group Role, hapus seluruh baris group di tabel hingga tersisa 0 group
2. Klik tombol `[Save]`
3. Verifikasi dialog blok muncul: Title `"Cannot Save Group Role"`, body bullet nama role dan kalimat `"At least one group must be assigned. To remove all access, turn off the role switch."` serta tombol `[OK]`
4. Klik `[OK]`, verifikasi popup tetap terbuka
5. Klik `[Clear Field]`, verifikasi tabel group dikosongkan namun popup tetap terbuka
6. Tambahkan group, ubah nilai, lalu klik icon `[✕]` di header
7. Verifikasi dialog konfirmasi muncul: `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` dan `[Leave]`
8. Klik `[Cancel]`, verifikasi kembali ke popup dengan isian tetap utuh
9. Klik `[✕]` lagi lalu klik `[Leave]`, verifikasi popup tertutup dan seluruh draft perubahan dibuang

## Notes

- Group Role wajib memiliki setidaknya 1 group ter-assign sebelum dapat disimpan dalam status aktif.
