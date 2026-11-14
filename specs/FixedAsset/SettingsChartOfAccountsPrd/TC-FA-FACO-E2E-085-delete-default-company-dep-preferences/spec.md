---
id: TC-FA-FACO-E2E-085-delete-default-company-dep-preferences
title: "Delete akun yang menjadi nilai default company ditolak"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [D-06, D-12, FACO-LOGIC-03b, "§9.2#p2", "§[F-FACO-05] Delete Account#r2", "§[F-FACO-05] Delete Account#r6", "§9.4.2#r17", "§9.4.2#r21"]
smoke: []
dependsOn: ["Settings > Accounting > Preferences: akun default company", "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  D-06: [10, 11, 13, 16, 17, 18, 19, 21]
  D-12: [26, 27, 28, 30, 31]
  FACO-LOGIC-03b: [10, 13, 17, 18, 27]
  "§9.2#p2": [7, 10]
  "§[F-FACO-05] Delete Account#r2": [10, 16, 17, 18]
  "§[F-FACO-05] Delete Account#r6": [26, 27, 30, 31, 34]
  "§9.4.2#r17": [10, 13, 17, 18, 21]
  "§9.4.2#r21": [26, 27, 30, 31, 34]
anchor: [6]
coverage:
  web: automated
---
# Delete akun yang menjadi nilai default company ditolak

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-085-1: Account Code `DDC1-{runId}`, Account Name `Gain Disposal Default {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By `0`, belum pernah diekspor, nilai `Default Gain on Disposal` di Preferences, ada di entitas aktor.
  - DU-085-2: Account Code `DDC2-{runId}`, Account Name `Loss Disposal Default {runId}`, Account Function `Loss on Disposal`, Status `Active`, Used By `1` (dipakai 1 Asset Class), belum pernah diekspor, nilai `Default Loss on Disposal` di Preferences, ada di entitas aktor.
  - Label akun pada bullet dialog dibentuk dari Account Code dan Account Name:
    - DU-085-1: `DDC1-{runId} – Gain Disposal Default {runId}`, dari Account Code `DDC1-{runId}` dan Account Name `Gain Disposal Default {runId}`.
    - DU-085-2: `DDC2-{runId} – Loss Disposal Default {runId}`, dari Account Code `DDC2-{runId}` dan Account Name `Loss Disposal Default {runId}`.
  - Kedua akun DU-085-1 dan DU-085-2 adalah seluruh akun milik spec ini.
- Kondisi: Settings > Accounting > Preferences menyimpan akun DU-085-1 sebagai nilai `Default Gain on Disposal` dan akun DU-085-2 sebagai nilai `Default Loss on Disposal` untuk entitas aktor.

## Test Steps

### Delete tunggal atas akun default company yang tidak dipakai Asset Class ditolak dengan alasan default company saja
1. Klik ikon `Changelog` di toolbar
2. Ketik Search `{runId}`, tekan Enter
3. Catat jumlah baris hasil Search di modal Changelog
4. Klik `✕` pada modal Changelog
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris `DDC1-{runId}` dan `DDC2-{runId}` tampil
7. Verifikasi Used By baris `DDC1-{runId}` bernilai `0` dan Used By baris `DDC2-{runId}` bernilai `1`, yaitu pemakaian sebagai default company tidak menambah Used By
8. Klik `⋯` pada baris `DDC1-{runId}`
9. Klik `Delete`
10. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `DDC1-{runId} – Gain Disposal Default {runId}` dan kalimat `This account is the default company account for Default Gain on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
11. Verifikasi dialog tidak memuat kalimat `This account is used by`, karena akun tidak dipakai Asset Class
12. Klik `[OK]`
13. Verifikasi baris `DDC1-{runId}` masih tampil di tabel

### Delete tunggal atas akun yang sekaligus dipakai Asset Class dan default company menampilkan dua alasan berurutan
14. Klik `⋯` pada baris `DDC2-{runId}`
15. Klik `Delete`
16. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `DDC2-{runId} – Loss Disposal Default {runId}`
17. Verifikasi dialog memuat kalimat `This account is used by 1 Asset Class and cannot be deleted.`
18. Verifikasi dialog memuat kalimat `This account is the default company account for Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
19. Verifikasi kalimat `This account is used by 1 Asset Class and cannot be deleted.` tampil lebih dahulu daripada kalimat `This account is the default company account for Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
20. Klik `[OK]`
21. Verifikasi baris `DDC2-{runId}` masih tampil di tabel

### Bulk Delete atas akun yang seluruhnya diblokir ditolak tanpa mengubah data dan tanpa log
22. Centang baris `DDC1-{runId}`
23. Centang baris `DDC2-{runId}`
24. Klik `Bulk Action`
25. Klik `Delete`
26. Verifikasi dialog `Cannot Delete Accounts` tampil dengan kelompok `The following are in use and cannot be deleted:` yang memuat bullet `DDC2-{runId} – Loss Disposal Default {runId}`
27. Verifikasi dialog memuat kelompok `The following are default company accounts and cannot be deleted:` dengan bullet `DDC1-{runId} – Gain Disposal Default {runId}` yang diikuti kalimat `This account is the default company account for Default Gain on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
28. Verifikasi bullet `DDC2-{runId} – Loss Disposal Default {runId}` tidak tampil lagi di kelompok `The following are default company accounts and cannot be deleted:`, karena akun itu sudah tampil di kelompok `The following are in use and cannot be deleted:`
29. Klik `[OK]`
30. Verifikasi baris `DDC1-{runId}` masih tampil di tabel
31. Verifikasi baris `DDC2-{runId}` masih tampil di tabel
32. Klik ikon `Changelog` di toolbar
33. Ketik Search `{runId}`, tekan Enter
34. Verifikasi jumlah baris hasil Search di modal Changelog sama dengan jumlah yang dicatat pada langkah 3, yaitu tidak ada entri log baru
35. Klik `✕` pada modal Changelog
