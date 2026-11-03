---
id: TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset
title: "Grace Period FA-7: Tab Accounting Read-Only dan Form Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-547
  - TC-FA-CF-662
  - TC-FA-CF-667
  - TC-FA-CF-672
  - TC-FA-CF-674
coverage:
  web: automated
---

# Grace Period FA-7: Tab Accounting Read-Only dan Form Aset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Grace (Pre-setup #25). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_GRACE_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Grace (Pre-setup #25): FA-7 sempat aktif lalu diturunkan ke None efektif T-0 dengan Grace Period berjalan (T+10 hari); field Accounting `Cost Center` Text General Active Required Yes bernilai `CC-100` pada aset `A1` dan kosong pada aset `A2`; `Asset Tag Class` Text General Inactive; field General `Asset Serial Tag` Active Required No bernilai pada `A1` dan `A2`. Nilai data mengacu `Fixture.faCustomFields.grace` (fixture belum ada, disediakan tim FE).
- Data Dinamis: nilai `Asset Serial Tag` aset `A2` hasil Edit: `Serial {runId}-145`.
- Kemampuan teknis: hover; Column Visibility Asset List; seed reset Company Grace (disediakan tim FE/BE); penghapusan preferensi Column Visibility Asset List yang disimpan di browser (disediakan tim FE, bagian 4).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: spec mengubah nilai `Asset Serial Tag` aset `A2` Company Grace (data Pre-setup, TC-FA-CF-674); hook `before` dan `after` memulihkannya lewat seed reset Company Grace. Hook `after` juga menghapus preferensi Column Visibility Asset List yang disimpan spec di browser pada langkah 24 (bukan `[Reset to Default]`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-547 dan TC-FA-CF-662: tab Accounting selama Grace Period

1. Arahkan kursor ke tab `Accounting`
2. Verifikasi tab `Accounting` tidak disabled
3. Verifikasi tab `Accounting` tanpa icon 🔒
4. Verifikasi tooltip `Accounting fields require the Accounting & Depreciation feature. Upgrade your plan to unlock them.` tidak muncul
5. Klik tab `Accounting`
6. Verifikasi tab `Accounting` terbuka
7. Verifikasi tabel grup Accounting memuat `Cost Center` (Active) dan `Asset Tag Class` (Inactive)
8. Verifikasi konfigurasi tersimpan kedua field tampil di tabel (Text, Scope General; `Cost Center` Required `Yes`)
9. Verifikasi toolbar Search, Download, dan Changelog tampil
10. Verifikasi tombol `[+ Custom Field]` Hidden
11. Verifikasi row action `Edit` dan `Delete` Hidden pada baris `Cost Center`
12. Verifikasi kolom Checkbox baris dan Bulk Action Bar Hidden
13. Arahkan kursor ke switch Active baris `Cost Center`
14. Verifikasi switch Active Disabled dengan tooltip `You don't have permission to do this.`

### TC-FA-CF-667: field Accounting di form registrasi, Detail, dan Asset List

15. Buka form registrasi aset pada modul Asset Registration
16. Verifikasi form registrasi aset tampil
17. Verifikasi `Cost Center` tidak tampil di form registrasi aset
18. Verifikasi `Cost Center` tidak diwajibkan pada form registrasi aset
19. Buka Detail aset `A1`
20. Verifikasi `Cost Center` tampil read-only di Detail aset `A1`
21. Verifikasi nilai `Cost Center` pada Detail aset `A1` adalah nilai tersimpan `CC-100`
22. Buka Asset List dan buka daftar Column Visibility
23. Verifikasi `Cost Center` tersedia sebagai kolom opsional di Column Visibility
24. Tampilkan kolom `Cost Center` lewat Column Visibility
25. Ketik Search `CC-100`, tekan Enter
26. Verifikasi aset `A1` ditemukan oleh Search `CC-100` (Data Type Text dapat dicari)
27. Klik `(←)` pada kotak Search

### TC-FA-CF-672: form Edit aset menampilkan field Accounting read-only

28. Buka form Edit aset `A1`
29. Verifikasi `Cost Center` tampil dengan nilai tersimpan `CC-100`
30. Verifikasi `Cost Center` tidak dapat diubah (read-only)

### TC-FA-CF-674: Required field Accounting tidak ditegakkan pada Edit aset

31. Buka form Edit aset `A2`
32. Ubah nilai `Asset Serial Tag` menjadi `Serial {runId}-145`
33. Simpan form Edit aset
34. Verifikasi perubahan tersimpan tanpa error
35. Verifikasi tidak ada error Required pada `Cost Center`
36. Buka Detail aset `A2`
37. Verifikasi Detail aset `A2` menampilkan nilai `Asset Serial Tag` baru `Serial {runId}-145`
38. Verifikasi `Cost Center` pada Detail aset `A2` tetap kosong

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: semua blok memakai satu kelas harness (kelas h, Company Grace dengan Grace Period berjalan), berdiri sendiri, dan hanya membaca kecuali langkah 31 sampai 38; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Klik tab `Accounting` di langkah 5 melayani Langkah 2 TC-FA-CF-547 dan Langkah 1 TC-FA-CF-662; langkah 6 adalah `Verifikasi` "Tab `Accounting` terbuka" (TC-FA-CF-662 Expected a) dan langkah 7 adalah Expected b TC-FA-CF-547.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 24 (menampilkan kolom lewat Column Visibility), langkah 27 (menutup Search), langkah 31 (membuka form Edit `A2` menggantikan form Edit `A1` yang tidak diubah). Search `CC-100` di langkah 25 dicatat sebagai langkah penghubung bagi Expected c TC-FA-CF-667 (R-16). Langkah 16 adalah anchor positif untuk absence `Cost Center` di form.
- Urutan Expected mengikuti urutan state (bagian 8b butir 5): Expected f TC-FA-CF-662 (toolbar tampil) diasersi di langkah 9 sebelum asersi Hidden sebagai anchor permukaan.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Grace (Pre-setup #25 hanya mendeskripsikan Company); akun disediakan tim FE.
  - Expected a TC-FA-CF-667 dan TC-FA-CF-674 menyebut `Cost Center` "tidak diwajibkan" tanpa langkah observasi; spec menurunkannya dari ketiadaan field di form (langkah 18) dan dari penyimpanan tanpa error (langkah 35).
  - TC-FA-CF-674 menyebut "Ubah nilai `Asset Serial Tag`" tanpa nilai; spec memakai nilai Dinamis `Serial {runId}-145`.
